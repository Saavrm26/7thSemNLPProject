from elasticsearch import Elasticsearch, helpers

from config import ELASTIC_SEARCH_CONN_URL
from dao.DAO import DataAccessObject


class ElasticSearchBM25DAO(DataAccessObject):
    def __init__(self, index_name, index_mapping):
        self.index_name = index_name
        self.index_mapping = index_mapping
        self.client = Elasticsearch(hosts=[ELASTIC_SEARCH_CONN_URL])
        self.create_index_if_not_exists()

    def create_index_if_not_exists(self):
        if self.client.indices.exists(index=self.index_name):
            return
        self.client.indices.create(index=self.index_name, body=self.index_mapping)

    def ingest(self, doc):
        self.client.index(index=self.index_name, document=doc)

    def bulk_ingest(self, docs):
        actions = [
            {
                "_index": self.index_name,
                "_source": doc
            }
            for doc in docs
        ]
        helpers.bulk(self.client, actions)

    def retrieve(self, query):
        response = self.client.search(index=self.index_name, query=query)
        hits = response['hits']['hits']
        return hits
