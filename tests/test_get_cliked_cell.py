import pygame
from main import *

def test_get_clicked_cell():
    # Create a list of cells
    cells = {}
    for row in range(3):
        for col in range(3):
            cells[(row, col)] = Cell(row, col)

    # Click on a cell in the middle of the grid
    click_location = pygame.math.Vector2(cells[(1, 1)].left + cells[(1, 1)].width // 2,
                                          cells[(1, 1)].top + cells[(1, 1)].height // 2)
    game = Game()
    clicked_cell = game.get_clicked_cell(click_location)
    assert clicked_cell == cells[(1, 1)]

