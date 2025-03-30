import unittest
from module3.module3 import function_from_module3

class TestModule3(unittest.TestCase):
    def test_function_from_module3(self):
        result = function_from_module3()
        self.assertEqual(result, "Mensagem do Módulo 3")

if __name__ == "__main__":
    unittest.main()
