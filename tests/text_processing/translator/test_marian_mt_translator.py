# MarianMT tests
import unittest
from text_processing.translator.marian_mt_translator import MarianMTTranslator


class TesteMarianMTTranslator(unittest.TestCase):
    def setUp(self):
        self.texto_teste = "Bonjour tout le monde"
        self.marian_tradutor = MarianMTTranslator()

    def test_marian_tradutor(self):
        result = self.marian_tradutor.translate(self.texto_teste)
        self.assertIsInstance(result, str)
        self.assertEqual('Hello, everybody.', result)

if __name__ == "__main__":
    unittest.main()