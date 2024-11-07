import config

import os

def list_files(directory):
    return [os.path.abspath(os.path.join(directory, f)) for f in os.listdir(directory)]

files = list_files("artifacts/data/")

print(files)