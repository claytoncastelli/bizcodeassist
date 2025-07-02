from abc import ABC, abstractmethod
from langdetect import detect


# BaseClass
class BaseTranslator(ABC):

    @abstractmethod
    def translate(self, texto: str) -> str:
        pass

    def detect_language(self, text: str) -> str:
        try:
            return detect(text)
        except:
            return "unknown"
