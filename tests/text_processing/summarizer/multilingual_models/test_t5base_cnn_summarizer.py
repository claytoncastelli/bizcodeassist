import unittest

# English models
from text_processing.summarizer.english_models.bart_samsum_summarizer import BartSamsumDialogue
from text_processing.summarizer.english_models.bart_summarizer import BartLargeCNN
from text_processing.summarizer.english_models.pegasus_cnn_summarizer import PegasusCNN
from text_processing.summarizer.english_models.pegasus_xsum_summarizer import PegasusXSUM
from text_processing.summarizer.english_models.t5_base_summarizer import T5BaseEnglish


# Multilingual models
from text_processing.summarizer.multilingual_models.mt5base_summarizer import MT5BaseSummarizer
from text_processing.summarizer.multilingual_models.mt5xlsum_summarizer import XLSumSummarizer
from text_processing.summarizer.multilingual_models.t5base_cnn_summarizer import PierreguillouSummarizer


class TestT5BasePtCNN(unittest.TestCase):
    def test_summary(self):
        model = PierreguillouSummarizer()
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