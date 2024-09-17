from abc import ABC, abstractmethod


class DataAccessObject(ABC):
    @abstractmethod
    def ingest(self, data):
        """Public method to ingest data into the data source."""
        pass

    @abstractmethod
    def retrieve(self, query):
        """Public method to retrieve data based on a query."""
        pass