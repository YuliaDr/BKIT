import unittest
from unittest.mock import Mock
from lab1 import get_roots


class RootsTest(unittest.TestCase):
    def test_roots(self):
        mock = Mock(return_value=4)
        self.assertEqual(get_roots(mock(), -5, 1), [1, -1, 0.5, -0.5])


if __name__ == "__main__":
    unittest.main()
