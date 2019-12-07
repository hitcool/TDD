import unittest
import funkcje

class Test(unittest.TestCase):

    def test_upper(self):
        wynik = funkcje.upper('string')
        self.assertEqual(wynik, 'STRING')

    def test_upper(self):
        pass

# ----------------------------------------
    def test_lower(self):
        wynik = funkcje.lower('Co to Jest ')
        self.assertEqual(wynik, 'co to jest')

    def test_lower(self):
        pass

# ----------------------------------------
    def test_title(self):
        wynik = funkcje.title('co to jest')
        self.assertEqual(wynik, 'Co To Jest')

    def test_title(self):
        pass



if __name__ == '__main__':
    unittest.main()
