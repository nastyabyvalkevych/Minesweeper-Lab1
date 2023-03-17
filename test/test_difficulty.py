import unittest
from main import Game

class TestGame(unittest.TestCase):
    def test_set_difficulty(self):
        game = Game()

        # check beginner difficulty
        game.set_difficulty('beginner')
        self.assertEqual(game.size, {'rows': 8, 'cols': 8})
        self.assertEqual(game.num_mines, 10)

        # check intermediate difficulty
        game.set_difficulty('intermediate')
        self.assertEqual(game.size, {'rows': 16, 'cols': 16})
        self.assertEqual(game.num_mines, 40)

        # check expert difficulty
        game.set_difficulty('expert')
        self.assertEqual(game.size, {'rows': 16, 'cols': 30})
        self.assertEqual(game.num_mines, 99)
