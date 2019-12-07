# import progamu unittest i program
import unittest
import program

# stworzymy klasy testowej dziedziczacej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):
    # zakladam ze w moim progam ma funkcje zwroc_100
    def test_zwroc_100(self):
        # wywylanie metody
        wynik = program.zwroc_100()
        # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
            # przykladowa funkcja, ktora bedzie sprawdzala metode
            # zwroc_100 z naszego programu
            # metoda powinna zwrocic liczbe 100
        self.assertEqual(wynik, 100)


    def test_zwroc_parametr(self):
        wynik = program.zwroc_parametr(124)
        self.assertEqual(wynik, 124)


# Hello World
    def test_hello(self):
        wynik = program.hello()
        self.assertEqual(wynik, 'Hello Test Driven Development')


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
        wynik = program.calc_div(3,3)
        self.assertEqual(wynik,2)






if __name__ == '__main__':
    unittest.main()
