from transformers import pipeline
from text_processing.summarizer.summarizer import SummarizerBase

class T5BaseEnglish(SummarizerBase):
    def __init__(self):
        # super().__init__(max_length=50, min_length=15, do_sample=False)
        self.max_length = 50
        self.min_length = 15
        self.do_sample = False
        self.pipeline = pipeline("summarization", model="t5-base")

    def summarize(self, text: str) -> str:
        result = self.pipeline("summarize: " + text, max_length=self.max_length, min_length=self.min_length, do_sample=self.do_sample)
        return result[0]['summary_text']