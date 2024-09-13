import os
from dotenv import load_dotenv
import nltk

load_dotenv()

URL = "https://services.nvd.nist.gov/rest/json/cves/2.0"
API_KEY = os.environ.get("API_key")
ELASTIC_SEARCH_CONN_URL = os.environ.get("ELASTIC_SEARCH_CONN_URL")

nltk.download('punkt')
nltk.download('stopwords')