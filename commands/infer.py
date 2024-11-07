import json
from collections import defaultdict

def extract_sequences(labeled_sequence):
    data = defaultdict(str)

    for (token, label) in labeled_sequence:
        if label == "O":
            continue
        if token == "[CLS]" or token == "[SEP]" or token == "[UNK]" or label == "[UNK]":
            continue
        bert_token = len(token) > 2 and token[:2] == "##"
        pos = label[0]
        t = label[2:]
        if pos == "B":
            data[t] += " || "
        else:
            data[t] += " " if not bert_token else ""
        data[t] += token if not bert_token else token[2:]

    return data

with open("./artifacts/predicted_bert.json", "r") as f: predicted_bert = json.load(f)
with open("./artifacts/predicted_crf.json", "r") as f: predicted_crf = json.load(f)

def get_pretty_data(predictions):
    pretty_data = []
    keys_to_exclude = ['tokens', 'predicted_description', 'labeled_description']
    for vuln in predictions:
        keys = [k for k in list(vuln.keys()) if k not in keys_to_exclude]
        data = {}
        for k in keys:
            data[k] = vuln[k]
        data = {**data, **extract_sequences(vuln['predicted_description'])}
        pretty_data.append(data)

    return pretty_data


bert_pretty_data = get_pretty_data(predicted_bert)
crf_pretty_data = get_pretty_data(predicted_crf)

with open("./artifacts/final_bert_results.json", "w") as f: f.write(json.dumps(bert_pretty_data, indent=4))
with open("./artifacts/final_crf_results.json", "w") as f: f.write(json.dumps(crf_pretty_data, indent=4))