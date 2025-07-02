from abc import ABC, abstractmethod


# BaseClass
class SummarizerBase(ABC):


    @abstractmethod
    def summarize(self, text: str) -> str:
        pass
