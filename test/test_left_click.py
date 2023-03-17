import pygame
from main import Game, Cell

def test_left_click():
    # create a new game
    game = Game()

    # create a test cell with a mine
    test_cell = Cell(0, 0, True)

    # place the test cell on the game board
    game.cells[(0, 0)] = test_cell

    # simulate a left-click on the test cell
    click_location = (test_cell.left + test_cell.width // 2, test_cell.top + test_cell.height // 2)
    game.left_click(click_location)

    # check that the test cell has been revealed
    assert test_cell.state == 'revealed'

    # check that the gameover flag has been set
    assert game.gameover == False
