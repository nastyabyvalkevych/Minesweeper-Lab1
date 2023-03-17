import pytest
from main import Game, Cell

def test_place_mines():
    # create a game instance
    game = Game()

    # create a clicked cell
    clicked_cell = Cell(3, 3)

    # place mines around the clicked cell
    game.place_mines(clicked_cell)

    # ensure that the number of mines placed is equal to the expected number
    assert sum(cell.has_mine for cell in game.cells.values()) == game.num_mines

    # ensure that none of the cells immediately surrounding the clicked cell have a mine
    for i in range(clicked_cell.row - 1, clicked_cell.row + 2):
        for j in range(clicked_cell.col - 1, clicked_cell.col + 2):
            if i >= 0 and i < game.size['rows'] and j >= 0 and j < game.size['cols']:
                assert not game.cells[(i, j)].has_mine

    # ensure that all other cells have a mine with a distance of at least 2 from the clicked cell
    for cell in game.cells.values():
        if cell != clicked_cell and not cell.has_mine:
            distance = ((cell.row - clicked_cell.row) ** 2 + (cell.col - clicked_cell.col) ** 2) ** 0.5
            assert distance >= 1