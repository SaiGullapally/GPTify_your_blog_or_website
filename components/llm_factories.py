from abc import ABC, abstractmethod
from langchain.chat_models import ChatOpenAI


class AbstractLLMFactory(ABC):
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
    def get_llm(self) -> object:
        """
        Returns:
            object: returns the appropriate embedding model
        """
        pass


class OpenAIGPT3p5Factory(AbstractLLMFactory):
    """class to instantiate and return OpenAI chat gpt 3.5 model
    """
    def __init__(self, api_key: str = None, temperature: float = 0) -> None:
        """initializes the parameters of the model factory
        Args:
            api_key (str): the open api key
        """
        self.api_key =  api_key
        self.temperature = temperature

    @abstractmethod
    def get_embeddings_model(self) -> object:
        """
        Returns:
            object: returns the appropriate openai embedding model
        """
        return ChatOpenAI(temperature= self.temperature, model_name='gpt-3.5-turbo', openai_api_key = self.api_key)
        