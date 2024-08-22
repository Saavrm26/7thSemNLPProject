import os
from dotenv import load_dotenv
load_dotenv();

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
API_KEY = os.environ.get("API_key")
