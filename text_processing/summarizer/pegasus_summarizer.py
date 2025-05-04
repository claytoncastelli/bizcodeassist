# pegasus_summarizer.py
from transformers import pipeline
from text_processing.summarizer.summarizer import BaseSummarizer

class PegasusSummarizer(BaseSummarizer):
    def __init__(self):
        print("[pegasus summarizer (150 <= word count <500 )]")
        self.summarizer = pipeline("summarization", model="google/pegasus-xsum")

    def summarize(self, text: str) -> str:
        return self.summarizer(text, truncation=True)[0]['summary_text']
