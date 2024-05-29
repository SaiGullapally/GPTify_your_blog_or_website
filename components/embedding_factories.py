from abc import ABC, abstractmethod
from langchain.embeddings import OpenAIEmbeddings


class AbstractEmbeddingsFactory(ABC):
    """Abstract class to define the signatures/contracts of the critical methods
    for the concrete factories to instantiale embeddings models
    """
    def __init__(self, api_key: str = None) -> None:
        """initializes the parameters of the model factory
        Args:
            api_key (str): the api key to connect to the cloud service
        """
        self.api_key =  api_key


    @abstractmethod
    def get_embeddings_model(self) -> object:
        """
        Returns:
            object: returns the appropriate embedding model
        """
        pass


class OpenAIEmbeddingsFactory(AbstractEmbeddingsFactory):
    """class to instantiate and return OpenAI embeddings model
    """
    def __init__(self, api_key: str = None) -> None:
        """initializes the parameters of the model factory
        Args:
            api_key (str): the open api key
        """
        self.api_key =  api_key

    @abstractmethod
    def get_embeddings_model(self) -> object:
        """
        Returns:
            object: returns the appropriate openai embedding model
        """
        return OpenAIEmbeddings(openai_api_key = self.api_key)
        