from abc import ABC, abstractmethod


# BaseClass
class BaseTranslator(ABC):

    @abstractmethod
    def traduzir(self, texto: str) -> str:
        pass
