from abc import ABC, abstractmethod


# BaseClass
class BaseSummarizer(ABC):

    @abstractmethod
    def summarize(self, text: str) -> str:
        pass
