# MarianMT  Implementation
from text_processing.translator.translator import BaseTranslator
from transformers import MarianTokenizer, MarianMTModel

class MarianMTTranslator(BaseTranslator):
    def __init__(self):
        self.model_name = "Helsinki-NLP/opus-mt-fr-en"
        self.tokenizer = MarianTokenizer.from_pretrained(self.model_name)
        self.model = MarianMTModel.from_pretrained(self.model_name)

    def translate(self, texto: str) -> str:
        inputs = self.tokenizer(texto, return_tensors="pt", padding=True, truncation=True)
        translation = self.model.generate(**inputs)
        return self.tokenizer.batch_decode(translation, skip_special_tokens=True)[0]