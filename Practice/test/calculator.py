import unittest
from ReynelSanchez.Practice.src.calculator import Calculator


class CalculatorTest(unittest.TestCase):
    def test_add(self):
        cal = Calculator()
        result = cal.add(2, 2)
        self.assertEqual(4, result)

    def test_valid_age(self):
        cal = Calculator()
        result = cal.valid_age(5)
        self.assertTrue(result)

    def test_invalid_age(self):
        cal = Calculator()
        result = cal.valid_age(-5)
        self.assertFalse(result)

    def test_max(self):
        cal = Calculator()
        result = cal.max(5,5,4)
        self.assertEqual(5,result)

    def test_isVocal(self):
        cal = Calculator()
        result = cal.isVocal('a')
        self.assertEqual('a', result)

    def test_inversa(self):
        cal = Calculator()
        result = cal.inverse('hola')
        self.assertEqual('aloh', result)

    def test_palindromo(self):
        cal = Calculator()
        result = cal.palindromo('ana')
        self.assertTrue(result)

    def test_mayorMenorPromedio(self):
        cal = Calculator()
        result = cal.mayorMenorPromedio([2, 10, 5, 3])
        self.assertEqual([10, 2, 5], result)

    def test_paises(self):
        cal = Calculator()
        result = cal.paises(['bolivia', 'chile', 'peru', 'estados unidos', 'jamaica', 'colombia'])
        self.assertEqual('estados unidos', result)

    def test_binario(self):
        cal = Calculator()
        result = cal.binario(10)
        self.assertEqual(1010, result)

    def test_cantidad_caracteres(self):
        cal = Calculator()
        result = cal.cantidad_caracteres('hola como estas Paolo')
        self.assertEqual(21, result)


