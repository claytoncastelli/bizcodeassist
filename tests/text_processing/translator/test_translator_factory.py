import unittest

from text_processing.translator.google_translator import GoogleTranslator
from text_processing.translator.marian_mt_translator import MarianMTTranslator
from text_processing.translator.mt_translate import MTranslator
from text_processing.translator.tradutor_factory import TranslatorFactory
from text_processing.translator.translator_type import TranslatorType


class TestTranslatorFactory(unittest.TestCase):
    def test_create_marianmt(self):
        tradutor = TranslatorFactory.create_translator(TranslatorType.MARIANMT)
        self.assertIsInstance(tradutor, MarianMTTranslator)

    def test_create_googletrans(self):
        tradutor = TranslatorFactory.create_translator(TranslatorType.GOOGLETRANS)
        self.assertIsInstance(tradutor, GoogleTranslator)

    def test_create_mtranslate(self):
        tradutor = TranslatorFactory.create_translator(TranslatorType.MTRANSLATE)
        self.assertIsInstance(tradutor, MTranslator)

    def test_create_tradutor_invalido(self):
        with self.assertRaises(ValueError):
            TranslatorFactory.create_translator("invalid")

if __name__ == "__main__":
    unittest.main()