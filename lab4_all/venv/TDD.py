import unittest
from lab1 import get_roots

class RootsTest(unittest.TestCase):
    def test_roots(self):
        self.assertEqual(get_roots(4, -5, 1), [1, -1, 0.5, -0.5])
        self.assertEqual(get_roots(1, -2, -8), [2, -2])
        self.assertEqual(get_roots(1, 11, 10), [])

if __name__ == "__main__":
    unittest.main()