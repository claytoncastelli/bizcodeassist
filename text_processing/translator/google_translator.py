# Googletrans  Implementation
from text_processing.translator.translator import BaseTranslator
from googletrans import Translator

class GoogleTranslator(BaseTranslator):
    def __init__(self):
        self.translator = Translator()

    def translate(self, text: str) -> str:
        src_lang = self.detect_language(text)
        result = text
        if src_lang == "fr":
            result =  self.translator.translate(text, src="fr", dest="en").text
        elif src_lang == "en":
            result = text
        else:
            raise Exception(f"unsupported language {src_lang}")
        return result

