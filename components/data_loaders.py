import os
from abc import ABC, abstractmethod


class AbstractDataLoader(ABC):
    """Abstract class to define the signatures/contracts of the critical methods
    for the concrete factories to store load data
    """

    @abstractmethod
    def load_data(self, data_dir: str) -> str:
        """Loads the data

        Args:
            data_dir (str): the root dir from which to load the data

        Returns:
            object: returns all the data concatenated as a string
        """
        pass


class TxtDataLoader(AbstractDataLoader):
    """class to load and return data from all .txt documents in the given folder"""

    def load_data(self, data_dir: str) -> str:
        """Loads the data

        Args:
            data_dir (str): the root dir from which to load the data
        Returns:
            object: returns all the data from .txt file within the data dir, concatenated into a string
        """
        txt_files = [
            os.path.join(data_dir, f)
            for f in os.listdir(data_dir)
            if f.endswith(".txt")
        ]
        print(f"reading data from: {txt_files}")
        text = ""
        for file in txt_files:
            with open(file) as f:
                text += f.read()
                text += "\n\n"
        print("completed reading the text data")
        return text
