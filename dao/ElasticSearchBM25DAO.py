from elasticsearch import Elasticsearch
import re
from dao.DAO import DataAccessObject
from config import ELASTIC_SEARCH_CONN_URL


class ElasticSearchBM25DAO(DataAccessObject):
    def __init__(self, index_name):
        self.index_name = index_name
        self.client = Elasticsearch(hosts=[ELASTIC_SEARCH_CONN_URL])

    def ingest(self, text):
        processed_sentences = self.__preprocess(text)
        for i, sentence in enumerate(processed_sentences):
            doc = {"sentence": sentence}
            self.client.index(index=self.index_name, document=doc)
            print(f"Ingested: {sentence}")

    def retrieve(self, query):
        response = self.client.search(index=self.index_name, query={"match": {"sentence": query}})
        hits = response['hits']['hits']
        print(f"Retrieved {len(hits)} results.")
        return [hit['_source']['sentence'] for hit in hits]

    def __preprocess(self, text):
        """Apply common NLP preprocessing techniques: lowercasing, removing special characters, and tokenizing sentences."""
        # Convert to lowercase
        text = text.lower()
        # Remove special characters (except punctuation for sentence splitting)
        text = re.sub(r'[^a-z0-9\s.]+', '', text)
        # Split into sentences
        sentences = [sentence.strip() for sentence in text.split('.') if sentence]
        return sentences
