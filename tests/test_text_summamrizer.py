import unittest
from text_processing.summarizer.text_summarizer import TextSummarizer

class TestTextSummarizer(unittest.TestCase):
    def setUp(self):
        self.summarizer = TextSummarizer()

    def test_summary_length(self):
        text = "This is a long text that needs to be summarized."
        summary = self.summarizer.summarize(text)
        self.assertLess(len(summary), len(text))

    def test_summary_not_empty(self):
        text = "AI is transforming the world."
        summary = self.summarizer.summarize(text)
        self.assertTrue(summary.strip())

if __name__ == "__main__":
    unittest.main()
