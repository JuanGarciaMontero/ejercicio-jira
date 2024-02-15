import unittest
from calculadora import sumar, restar, multiplicar, dividir

class TestCalculadora(unittest.TestCase):
    def test_calculadora(self):
        self.assertEqual(sumar(3, 2), 5)
        self.assertEqual(sumar(-1, 1), 0)
        self.assertEqual(sumar(-1, -1), -2)
        self.assertEqual(restar(3, 2), 1)
        self.assertEqual(restar(-1, 1), -2)
        self.assertEqual(restar(-1, -1), 0)
        self.assertEqual(multiplicar(3, 2), 6)
        self.assertEqual(multiplicar(-1, 1), -1)
        self.assertEqual(multiplicar(-1, -1), 1)
        self.assertEqual(dividir(3, 2), 1.5)
        self.assertEqual(dividir(-1, 1), -1)
        self.assertEqual(dividir(-1, -1), 1)
        self.assertEqual(dividir(5, 0), 'No se puede dividir por 0.')


if __name__ == '__main__':
    unittest.main()