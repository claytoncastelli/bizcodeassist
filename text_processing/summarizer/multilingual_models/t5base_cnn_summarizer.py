from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from text_processing.summarizer.summarizer import SummarizerBase

class PierreguillouSummarizer(SummarizerBase):
    def __init__(self, model_name="pierreguillou/t5-base-pt-summarizer-cnn-multilingual", prefix="summarize:"):
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
        self.prefix = prefix

    def summarize(self, text: str) -> str:
        input_text = self.prefix + " " + text
        print(f" summry **** {text}")

        inputs = self.tokenizer(text, return_tensors="pt", truncation=True)
        summary_ids = self.model.generate(inputs["input_ids"], max_length=100, min_length=20, do_sample=False)
        summary = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary