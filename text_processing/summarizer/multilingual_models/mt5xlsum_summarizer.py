from transformers import MT5Tokenizer, MT5ForConditionalGeneration
from text_processing.summarizer.summarizer import SummarizerBase

class XLSumSummarizer(SummarizerBase):
    def __init__(self, model_name="csebuetnlp/mT5_multilingual_XLSum"):
        self.tokenizer = MT5Tokenizer.from_pretrained(model_name)
        self.model = MT5ForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text: str) -> str:
        print(f" summry **** {text}")
        inputs = self.tokenizer(text, return_tensors="pt", truncation=True, max_length=512)
        summary_ids = self.model.generate(inputs.input_ids, max_length=128, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)