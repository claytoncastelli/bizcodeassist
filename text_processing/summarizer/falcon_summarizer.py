# pegasus_xsum_summarizer.py
from transformers import pipeline
from text_processing.summarizer.summarizer import BaseSummarizer

# https://huggingface.co/docs/transformers/main_classes/pipelines
class FalconSummarizer(BaseSummarizer):
    def __init__(self):
        print("[falcon summarizer (word count >=500)]")
        self.summarizer = pipeline("summarization", model="tiiuae/falcon-rw-1b")

    def summarize(self, text: str) -> str:
        return self.summarizer(text, truncation=True)[0]['summary_text']

