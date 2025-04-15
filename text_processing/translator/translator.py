from abc import ABC, abstractmethod


# BaseClass
class BaseTranslator(ABC):

    @abstractmethod
    def translate(self, texto: str) -> str:
        pass
