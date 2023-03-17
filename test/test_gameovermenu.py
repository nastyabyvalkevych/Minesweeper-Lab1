import unittest
from main import pygame_menu, Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game() # create an instance of the Game class

    def test_display_gameover_menu(self):
        heading = 'Game Over'
        self.game.display_gameover_menu(heading)
        labels = [widget for widget in self.game.gameover_menu.get_widgets() if isinstance(widget, pygame_menu.widgets.Label)]
        self.assertEqual(len(labels), 1) # check that only one label was added
        self.assertEqual(labels[0].get_title(), 'You clicked on a mine!') # check that the label has the correct text

