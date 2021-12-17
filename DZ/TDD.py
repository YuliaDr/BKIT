import unittest
import bot


class Test(unittest.TestCase):
    def testOperation(self):
        bot.first_num("6")
        bot.second_num("7")

        self.assertEqual(bot.operation("*"), 42)
        self.assertEqual(bot.operation("+"), 13)


if __name__ == "__main__":
    unittest.main()
