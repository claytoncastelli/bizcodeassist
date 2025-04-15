import unittest

from text_processing.translator.translator_factory import TranslatorFactory
from text_processing.translator.translator_type import TranslatorType


class TesteFAIRSEQ(unittest.TestCase):

    def setUp(self):
        self.texto_teste = "Bonjour tout le monde"
        self.fairseq_translator = TranslatorFactory.create_translator(TranslatorType.FAIRSEQ)

    def test_fairseq_tradutor(self):
        with self.assertRaises(NotImplementedError):
            result = self.fairseq_translator.translate(self.texto_teste)

        # result = self.fairseq_translator.translate(self.texto_teste)
        # self.assertIsInstance(result, str)
        # self.assertEqual('Hello everyone', result)
        # print("Fairseq:", result)
        #  print(self.texto_teste)