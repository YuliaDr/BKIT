import unittest
import main


class Test(unittest.TestCase):
    def test_t1(self):
        self.assertEqual(main.t1(), [('while', 5, 'Python'), ('do while', 3, 'C++')])

    def test_tk2(self):
        self.assertEqual(main.t2(), [('Python', 5.0), ('C++', 8.33), ('Java', 10.0), ('JS', 20.0)])

    def test_tk3(self):
        self.assertEqual(main.t3(), [('for', ['Java', 'JS', 'Python']), ('function', ['JS', 'Python'])])


if __name__ == "__main__":
    unittest.main()