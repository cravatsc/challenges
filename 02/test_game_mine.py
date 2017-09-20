import unittest
import game


class TestGame(unittest.TestCase):

    def setUp(self):
        self.test_board = game.UserBoard()
        self.test_board.letters = ['A', 'B', 'C', 'D']

    def test_word_from_letters(self):
        self.assertTrue(self.test_board._word_from_letters('cab'))
        self.assertFalse(self.test_board._word_from_letters('crab'))


if __name__ == '__main__':
    unittest.main()
