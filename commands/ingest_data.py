import json
import multiprocessing
import os

from dao import ElasticSearchBM25DAO
from nlp_preprocessor import lower_case, tokenize, lemmatize, remove_stopwords, ner, apply
from tenacity import retry, stop_after_attempt, wait_exponential


def preprocess_description(desc):
    extraction_pipeline = [lower_case, tokenize, remove_stopwords, lemmatize]
    ner_pipeline = [ner]

    named_entities = apply(desc, ner_pipeline)
    desc = apply(desc, extraction_pipeline)
    return {
        "description": " ".join(desc),
        "named_entities": [named_entity[0] for named_entity in named_entities]
    }

retry_decorator = retry(stop=stop_after_attempt(3), wait=wait_exponential(multiplier=1, min=4, max=10))

# @retry_decorator
def bulk_ingest(file_path):
    index_name = "test"
    from dao import es_base_index_mapping

    with open(file_path, 'r') as file:
        docs = json.load(file)
    print("Desearlized", file_path)
    # Get an instance from the DAO pool and ingest the documents
    dao = ElasticSearchBM25DAO(index_name, es_base_index_mapping)
    dao.bulk_ingest(docs)
    print("Ingested", file_path)


# Function to bulk ingest data from a directory using multiprocessing
def bulk_ingest_from_directory():
    data_directory = os.path.join(os.getcwd(), "artifacts/data")

    # Get all JSON file paths from the data directory
    file_paths = [os.path.join(data_directory, file) for file in os.listdir(data_directory) if file.endswith('.json')]
    num_processes = multiprocessing.cpu_count()

    # Use multiprocessing to process the files in parallel
    with multiprocessing.Pool(processes=num_processes) as pool:
        pool.starmap(bulk_ingest, [(file_path,) for file_path in file_paths])
        # pool.close()
        # pool.join()

    print("Data ingestion completed.")
