# import progamu unittest i program
import unittest
import program

# stworzymy klasy testowej dziedziczacej po klasie TestCase z modulu  unittest
class TestCALC(unittest.TestCase):

# kalkulator
    def test_calc(self):
        wynik = program.calc_add(1,3)
        self.assertEqual(wynik,4)

    def test_calc(self):
        wynik = program.calc_sub(5,3)
        self.assertEqual(wynik,2)

    def test_calc(self):
        wynik = program.calc_mul(1,3)
        self.assertEqual(wynik,3)

    def test_calc(self):
        wynik = program.calc_div(6,3)
        self.assertEqual(wynik,2)


if __name__ == '__main__':
    unittest.main()
