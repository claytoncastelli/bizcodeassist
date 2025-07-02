# from transformers import pipeline
from text_processing.summarizer.summarizer import SummarizerBase
from transformers import PegasusTokenizer, PegasusForConditionalGeneration

class PegasusCNN(SummarizerBase):
    def __init__(self, model_name = "google/pegasus-cnn_dailymail"):
        self.tokenizer = PegasusTokenizer.from_pretrained(model_name)
        self.model = PegasusForConditionalGeneration.from_pretrained(model_name)

    def summarize(self, text: str) -> str:

        inputs = self.tokenizer(text, truncation=True, padding="longest", return_tensors="pt")
        summary_ids = self.model.generate(**inputs, max_length=60, min_length=20, do_sample=False)
        summary  = self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
        return summary