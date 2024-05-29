from abc import ABC, abstractmethod

from langchain.vectorstores import Chroma


class AbstractWrappedVectorDB(ABC):
    """Abstract class to define the signatures/contracts of the critical methods
    for the concrete factories to instantiale embeddings models
    """

    def __init__(self, k: str = None) -> None:
        """initializes the parameters of the vector db
        Args:
            k (str): the number of nearest neighbors to search for
        """
        self.k = k
        self.db = None

    @abstractmethod
    def create_vector_db_from_texts(self) -> object:
        """
        Returns:
            object: returns the appropriate embedding model
        """
        pass

    @abstractmethod
    def create_vector_db_from_documents(self) -> object:
        """
        Returns:
            object: returns the appropriate embedding model
        """
        pass


class WrappedChromaVectorDB(AbstractWrappedVectorDB):
    """Abstract class to define the signatures/contracts of the critical methods
    for the concrete factories to instantiale embeddings models
    """

    def __init__(self, k: str = None) -> None:
        """initializes the parameters of the vector db
        Args:
            k (str): the number of nearest neighbors to search for
        """
        self.k = k
        self.db = None

    def create_vector_db_from_texts(self, texts, embeddings_model) -> object:
        """
        Returns:
            object: creates and returns the vector db from the inputs
        """
        return Chroma.from_texts(texts=texts, embedding=embeddings_model)

    def create_vector_db_from_documents(self, documents, embeddings_model) -> object:
        """
        Returns:
            object: creates and returns the vector db from the inputs
        """
        return Chroma.from_documents(documents=documents, embedding=embeddings_model)
