# MTranslate tests
import unittest
from text_processing.translator.mt_translate import MTranslator


# Classes de Testes
class TesteMTranslator(unittest.TestCase):
    def setUp(self):
        self.texto_teste = "Bonjour tout le monde"
        self.mtranslate_tradutor = MTranslator()

    def test_mtranslate_tradutor(self):
        result = self.mtranslate_tradutor.traduzir(self.texto_teste)
        self.assertIsInstance(result, str)
        self.assertEqual('Hello everyone', result)
        print("MTranslate:", result)

if __name__ == "__main__":
    unittest.main()