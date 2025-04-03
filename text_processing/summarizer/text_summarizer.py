from transformers import pipeline

class TextSummarizer:
    def __init__(self, model_name="facebook/bart-large-cnn"):
        self.summarizer = pipeline("summarization", model=model_name)

    def summarize(self, text, max_length=200, min_length=50):
        word_count = len(text.split())
        if word_count < min_length // 2:
            return text  # Return original if too short

        adjusted_max_length = min(max_length, word_count)
        adjusted_min_length = min(min_length, word_count // 2)

        summary = self.summarizer(text, max_length=adjusted_max_length, min_length=adjusted_min_length, do_sample=False)
        print("[summary]: ", summary)
        print("[summary][0][summary_text]: ", summary[0]["summary_text"])

        return summary[0]["summary_text"]

if __name__ == "__main__":
    summarizer = TextSummarizer()
    
    text = """
    Our company provides AI-powered analytics solutions for optimizing business operations.
    We offer services ranging from data collection to predictive modeling, ensuring clients gain
    valuable insights. Our technology is widely used in finance, healthcare, and retail industries.
    """
    
    summary = summarizer.summarize(text)
    print("Original Text:", text)
    print("\nSummarized Text:", summary)
