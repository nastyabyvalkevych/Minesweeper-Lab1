import unittest
from main import pygame_menu, Game


class TestGame(unittest.TestCase):
    def test_create_custom_theme(self):
        self.game = Game()
        theme = self.game.create_custom_theme()

        self.assertEqual(theme.title_font, pygame_menu.font.FONT_NEVIS)
        self.assertEqual(theme.widget_font, pygame_menu.font.FONT_COMIC_NEUE)
        self.assertEqual(theme.widget_font_size, 25)
        self.assertEqual(theme.title_font_color, (80, 80, 90))
        self.assertEqual(theme.title_bar_style, pygame_menu.widgets.MENUBAR_STYLE_NONE)
        self.assertEqual(theme.title_close_button_cursor, pygame_menu.locals.CURSOR_HAND)