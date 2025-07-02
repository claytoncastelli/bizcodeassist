# MTranslate  Implementation
from text_processing.translator.translator import BaseTranslator
from mtranslate import translate

class MTranslator(BaseTranslator):
    def translate(self, text: str) -> str:
        src_lang = self.detect_language(text)
        result = text
        if src_lang == "fr":
            result = translate(text, "en", "fr")
        elif src_lang == "en":
            result = text
        else:
            raise Exception(f"unsupported language {src_lang}")
        return result
