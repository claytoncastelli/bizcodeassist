# Googletrans  Implementation
from text_processing.translator.translator import BaseTranslator
from googletrans import Translator

class GoogleTranslator(BaseTranslator):
    def __init__(self):
        self.translator = Translator()

    def traduzir(self, texto: str) -> str:
        return self.translator.translate(texto, src="fr", dest="en").text