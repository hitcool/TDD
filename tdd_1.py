# import progamu unittest i program
import unittest
import program

# stworzymy klasy testowe dziedziczacej po klasie TestCase z modulu  unittest
class TestTDD1(unittest.TestCase):


    def test_zwroc_100(self):
        # wywolanie metody
        wynik = program.zwroc_100()
        # sle dla klasy z unittest jak i naszej. Porownanie wynik z liczba 100
            # przykladowa funkcja, ktora bedzie sprawdzala metode
            # zwroc_100 z naszego programu
            # metoda powinna zwrocic liczbe 100
        self.assertEqual(wynik, 100)


    def test_zwroc_parametr(self):
        wynik = program.zwroc_parametr(124)
        self.assertEqual(wynik, 124)


    def test_hello(self):
        wynik = program.hello()
        self.assertEqual(wynik, 'Hello Test Driven Development')


if __name__ == '__main__':
    unittest.main()
