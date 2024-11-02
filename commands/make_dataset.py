import config
import json
import uuid
import asyncio
import os
import datetime

from models.llm_sequence_labeling import LlmSequenceLabelingModel

def list_files(directory):
    return [os.path.abspath(os.path.join(directory, f)) for f in os.listdir(directory)]

files = list_files("./artifacts/data/")

NUM_PROCESSES = 4

async def process_vulnerability(vulnerability):
    processing_id = id(vulnerability)
    print(f"{processing_id}: Admitted.")
    # await asyncio.sleep(random.uniform(0, 1.5))
    print(f"{processing_id}: Sending to LLM...")
    model = LlmSequenceLabelingModel("OPENAI")
    labeled_description = await model.async_invoke(vulnerability["description"])
    print(f"{processing_id} Processed!")
    return {**vulnerability, "labeled_description" : labeled_description}

async def add_wait(seconds):
    await asyncio.sleep(seconds)

async def worker(file_paths):
    loop = asyncio.get_event_loop()
    # loop = asyncio.new_event_loop()
    # asyncio.set_event_loop(loop)

    vulnerabilities = []
    for file_path in file_paths:
        file = open(file_path, "r")
        vulnerabilities.extend(json.load(file))

    batch_size = 500

    # promises = [process_vulnerability(vulnerability) for vulnerability in vulnerabilities]
    vulnerabilities_batches = [vulnerabilities[i:i + batch_size] for i in range(0, len(vulnerabilities), batch_size)]
    results = []

    for batch in vulnerabilities_batches:
        print(f"{datetime.datetime.now().strftime('%H:%M:%S')} : Starting")
        res = await asyncio.gather(*[process_vulnerability(vulnerability) for vulnerability in batch])
        with open(f"./artifacts/dataset_cache/{uuid.uuid4()}.json", "w") as f: f.write(json.dumps(res, indent=4))
        results.extend(res)
        print("Cached! Relaxing...")
        await add_wait(120)

    return results

# def make_dataset():
#     # chunk_size = len(files) // NUM_PROCESSES
#     #
#     # # Divide the list into equal-sized chunks
#     # chunks = [files[i:i + chunk_size] for i in range(0, len(files), chunk_size)]
#     #
#     # with multiprocessing.Pool(processes=NUM_PROCESSES) as pool:
#     #     results = pool.map(worker, chunks)
#     #
#     # with open("cache", "w") as f: f.write(json.dumps(results))
#     #
#     # with open("artifacts/dataset.json", "w") as f:
#     #     json_string = json.dumps([vulnerability for result in results for vulnerability in result], indent=4)
#     #     f.write(json_string)
#     worker(files)

if __name__ == "__main__":
    # make_dataset()
    asyncio.run(worker(files))
