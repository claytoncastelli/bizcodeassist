# pegasus_summarizer.py
from transformers import pipeline
from text_processing.summarizer.summarizer import BaseSummarizer

class BartSummarizer(BaseSummarizer):
    def __init__(self):
        print("[bart summarizer (word count < 150)]")
        self.summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

    def summarize(self, text: str) -> str:
        return self.summarizer(text, truncation=True)[0]['summary_text']
