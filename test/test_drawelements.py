import unittest
import pygame_menu
from main import Game, Cell


class TestGame(unittest.TestCase):

    def setUp(self):
        self.game = Game()

    def test_create_cells(self):
        # Виклик методу створення клітинок
        self.game.create_cells()

        # Перевірка, чи кількість створених клітинок дорівнює очікуваному значенню
        expected_cells_count = self.game.size['rows'] * self.game.size['cols']
        self.assertEqual(len(self.game.cells), expected_cells_count)

        # Перевірка, чи всі клітинки належать до класу Cell
        for cell in self.game.cells.values():
            self.assertIsInstance(cell, Cell)

        # Перевірка, чи всі клітинки мають унікальну позицію
        positions = set()
        for (row, col), cell in self.game.cells.items():
            self.assertNotIn((row, col), positions)
            positions.add((row, col))

    def test_draw_cells(self):
        self.game.create_cells()
        self.game.draw_cells()


    def test_draw_top_panel(self):
        self.game.draw_top_panel()

