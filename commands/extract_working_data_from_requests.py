import os
import json
from multiprocessing import Pool


def extract_working_data_from_requests(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)

    vulnerabilities = data.get('vulnerabilities', [])
    extracted_data = []

    for vuln in vulnerabilities:
        cve = vuln.get('cve', {})
        extracted_entry = {
            'id': cve.get('id'),
            'cveTags': cve.get('cveTags', [])
        }

        descriptions = cve.get('descriptions', [])
        en_description = next((desc.get('value') for desc in descriptions if desc.get('lang') == 'en'), None)
        extracted_entry['description'] = en_description

        metrics = cve.get('metrics', {})
        cvss_metrics = {key: metrics[key] for key in metrics if key.startswith('cvss')}
        extracted_entry['metrics'] = cvss_metrics

        extracted_data.append(extracted_entry)

    output_file = os.path.join(os.getcwd(), "artifacts/data")
    with open(output_file, 'w') as out_f:
        json.dump(extracted_data, out_f, indent=4)



def process_directory():
    directory = os.path.join(os.getcwd(), "artifacts/api_calls")
    print(f"Scanning directory {directory}")
    # List all JSON files in the directory
    json_files = [os.path.join(directory, file) for file in os.listdir(directory) if file.endswith('.json')]

    # Use multiprocessing to process files concurrently
    with Pool() as pool:
        pool.map(extract_working_data_from_requests, json_files)