import unittest
import main

class TestGame(unittest.TestCase):
    def right_guess(self):

        result=main.run_guess(5,5)
        self.assertTrue(result)

    def wrong_no(self):
        result = main.run_guess(6,5)
        self.assertFalse(result)

    def input_wrong_num(self):
        result = main.run_guess(6, 11)
        self.assertFalse(result)


if __name__ == '__main__':
    unittest.main()