import unittest
import pygame

from main import Game

class TestGame(unittest.TestCase):
    def test_init(self):
        game = Game()
        self.assertIsNotNone(game.window)
        # check pygame initialization
        self.assertTrue(pygame.get_init())
        self.assertEqual(pygame.font.get_default_font(), 'freesansbold.ttf')
