import unittest

from text_processing.summarizer.multilingual_models.mt5xlsum_summarizer import XLSumSummarizer

class TestMT5XLSum(unittest.TestCase):
    def test_summary(self):
        model = XLSumSummarizer()
        text = """The pipelines are a great and easy way to use models for inference. These pipelines are objects 
                that  abstract most of the complex code from the library, offering a simple API dedicated to several tasks, 
                including Named Entity Recognition, Masked Language Modeling, Sentiment Analysis, Feature Extraction and 
                Question Answering. See the task summary for examples of use."""
        summary = model.summarize(text)
        print(summary)
        self.assertIsInstance(summary, str)
        self.assertTrue(len(summary) > 10)

if __name__ == "__main__":
    unittest.main()