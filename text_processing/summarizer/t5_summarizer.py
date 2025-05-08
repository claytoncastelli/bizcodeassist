# text_processing/summarizer/t5_summarizer.py
from transformers import T5ForConditionalGeneration, T5Tokenizer
from text_processing.summarizer.summarizer import BaseSummarizer

class T5Summarizer(BaseSummarizer):
    def __init__(self, model_name="t5-small", device="cpu"):
        print("[t5 summarizer (word count >500)]")
        self.device = device
        self.tokenizer = T5Tokenizer.from_pretrained(model_name)
        self.model = T5ForConditionalGeneration.from_pretrained(model_name).to(device)

    def summarize(self, text: str) -> str:
        input_text = "summarize: " + text.strip().replace("\n", " ")
        inputs = self.tokenizer.encode(input_text, return_tensors="pt", max_length=512, truncation=True).to(self.device)
        summary_ids = self.model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        return self.tokenizer.decode(summary_ids[0], skip_special_tokens=True)
