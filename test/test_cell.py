import pygame
import unittest
from main import Cell

class TestCell(unittest.TestCase):
    def setUp(self):
        self.window = pygame.display.set_mode((400, 400))
        self.cell = Cell(0, 0)

    def test_constructor(self):
        self.assertEqual(self.cell.row, 0)
        self.assertEqual(self.cell.col, 0)
        self.assertEqual(self.cell.left, 0)
        self.assertEqual(self.cell.top, 50)
        self.assertEqual(self.cell.width, 50)
        self.assertEqual(self.cell.height, 50)
        self.assertEqual(self.cell.state, 'hidden')
        self.assertFalse(self.cell.has_mine)
        self.assertEqual(self.cell.clue, 0)

    def test_draw_hidden(self):
        self.cell.draw(self.window)


    def test_draw_revealed_mine(self):
        self.cell.has_mine = True
        self.cell.state = 'revealed'
        self.cell.draw(self.window)


    def test_draw_revealed_clue(self):
        self.cell.clue = 3
        self.cell.state = 'revealed'
        self.cell.draw(self.window)


    def test_draw_flagged(self):
        self.cell.state = 'flagged'
        self.cell.draw(self.window)


if __name__ == '__main__':
    unittest.main()
