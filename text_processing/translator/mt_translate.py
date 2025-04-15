# MTranslate  Implementation
from text_processing.translator.translator import BaseTranslator
from mtranslate import translate

class MTranslator(BaseTranslator):
    def translate(self, texto: str) -> str:
        return translate(texto, "en", "fr")