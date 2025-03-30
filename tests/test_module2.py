import unittest
from module2.module2 import function_from_module2

class TestModule2(unittest.TestCase):
    def test_function_from_module2(self):
        result = function_from_module2()
        self.assertEqual(result, "Mensagem do Módulo 2")

if __name__ == "__main__":
    unittest.main()
