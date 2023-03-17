import pytest
from main import Cell

def test_reveal():

    # create a 3x3 grid of cells with no mines
    cells = {}
    for row in range(3):
        for col in range(3):
            cells[(row, col)] = Cell(row, col)

    # reveal the center cell
    center_cell = cells[(1, 1)]
    revealed_count = center_cell.reveal(cells)

    # check that all cells are revealed
    assert center_cell.state == 'revealed'
    assert revealed_count == 9
    for row in range(3):
        for col in range(3):
            cell = cells[(row, col)]
            assert cell.state == 'revealed'


def test_reveal_with_mines():
    # create a 3x3 grid of cells with 2 mines
    cells = {}
    cells[(0, 0)] = Cell(0, 0, has_mine=True)
    cells[(0, 1)] = Cell(0, 1)
    cells[(0, 2)] = Cell(0, 2, has_mine=True)
    cells[(1, 0)] = Cell(1, 0, has_mine=True)
    cells[(1, 1)] = Cell(1, 1)
    cells[(1, 2)] = Cell(1, 2, has_mine=True)
    cells[(2, 0)] = Cell(2, 0, has_mine=True)
    cells[(2, 1)] = Cell(2, 1)
    cells[(2, 2)] = Cell(2, 2, has_mine=True)


    # reveal the center cell
    center_cell = cells[(1, 1)]
    revealed_count = center_cell.reveal(cells)

    # check that the center cell and its adjacent cells with no mine are revealed
    assert center_cell.state == 'revealed'
    assert revealed_count == 9
    if not center_cell.has_mine:
        for row, col in [(0, 1), (1, 1), (2, 1)]:
            cell = cells[(row, col)]
            assert cell.state == 'revealed'
            assert cell.has_mine == False
    else:
        assert revealed_count == 1

