# Googletrans tests
import unittest
from text_processing.translator.google_translator import GoogleTranslator


class TesteGoogleTranslate(unittest.TestCase):
    def setUp(self):
        self.texto_teste = "Bonjour tout le monde"
        self.google_tradutor = GoogleTranslator()

    def test_google_tradutor(self):
        result = self.google_tradutor.translate(self.texto_teste)
        self.assertIsInstance(result, str)
        self.assertEqual('Hello everyone', result)

if __name__ == "__main__":
    unittest.main()