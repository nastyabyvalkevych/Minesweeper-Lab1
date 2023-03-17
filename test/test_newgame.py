import unittest
from unittest.mock import MagicMock
from main import Game

class TestGame(unittest.TestCase):
    def test_new_game(self):
        self.game = Game()
        self.game.set_difficulty = MagicMock(return_value=None)
        self.game.setup_window = MagicMock(return_value=None)
        self.game.create_cells = MagicMock(return_value=None)
        self.game.main_menu.disable = MagicMock(return_value=None)

        self.game.new_game('beginner')

        self.assertFalse(self.game.gameover)
        self.assertEqual(self.game.revealed_count, 0)
        self.assertEqual(self.game.flag_count, 0)
