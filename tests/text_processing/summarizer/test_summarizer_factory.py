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

from text_processing.summarizer.summarizer_factory import SumarizerFactory


class TestSumarizerFactory(unittest.TestCase):

    def test_bart_samsum(self):
        summarizer = SumarizerFactory.create_sumarizer("philschmid/bart-large-cnn-samsum")
        self.assertIsInstance(summarizer, BartSamsumDialogue)

    def test_bart_large_cnn(self):
        summarizer = SumarizerFactory.create_sumarizer("facebook/bart-large-cnn")
        self.assertIsInstance(summarizer, BartLargeCNN)

    def test_pegasus_cnn(self):
        summarizer = SumarizerFactory.create_sumarizer("google/pegasus-cnn_dailymail")
        self.assertIsInstance(summarizer, PegasusCNN)

    def test_pegasus_xsum(self):
        summarizer = SumarizerFactory.create_sumarizer("google/pegasus-xsum")
        self.assertIsInstance(summarizer, PegasusXSUM)

    def test_t5_base(self):
        summarizer = SumarizerFactory.create_sumarizer("t5-base")
        self.assertIsInstance(summarizer, T5BaseEnglish)

    def test_mt5_base(self):
        summarizer = SumarizerFactory.create_sumarizer("google/mt5-base")
        self.assertIsInstance(summarizer, MT5BaseSummarizer)

    def test_xlsum(self):
        summarizer = SumarizerFactory.create_sumarizer("csebuetnlp/mT5_multilingual_XLSum")
        self.assertIsInstance(summarizer, XLSumSummarizer)

    # def test_pierreguillou(self):
    #     summarizer = SumarizerFactory.create_sumarizer("pierreguillou/t5-base-pt-summarizer-cnn-multilingual")
    #     self.assertIsInstance(summarizer, PierreguillouSummarizer)

    def test_invalid_model(self):
        with self.assertRaises(ValueError):
            SumarizerFactory.create_sumarizer("modelo/nao-existente")


if __name__ == "__main__":
    unittest.main()