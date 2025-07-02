# MarianMT  Implementation
from text_processing.translator.translator import BaseTranslator
from transformers import MarianTokenizer, MarianMTModel

class MarianMTTranslator(BaseTranslator):
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-fr-en"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def load_translation_model(self, src_lang):
        model_name = f"Helsinki-NLP/opus-mt-{src_lang}-en"
        self.tokenizers = MarianTokenizer.from_pretrained(model_name)
        self.models = MarianMTModel.from_pretrained(model_name)


    def translate(self, text: str) -> str:
        result = text
        src_lang = self.detect_language(text)
        print(f"found lamguage: {src_lang}")
        if src_lang != "en" and src_lang != "unknown" :
            self.load_translation_model(src_lang)
            tokenizer = self.tokenizers
            model = self.models
            inputs = tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
            translated = model.generate(**inputs, max_length=512, num_beams=4)
            result =tokenizer.decode(translated[0], skip_special_tokens=True)
        elif src_lang == "en":
            result = text
        else:
            raise Exception(f"unsupported language {src_lang}")
        return result