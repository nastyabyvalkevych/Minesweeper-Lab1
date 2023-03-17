import pytest
from main import *

def test_right_click():
    # Initialize a game
    game = Game()
    click_location = (100, 100)

    # Test clicking on an unrevealed cell
    cell = game.get_clicked_cell(click_location)
    assert cell.state == 'hidden'
    game.right_click(click_location)
    assert cell.state == 'flagged'
    assert game.flag_count == 1

    # Test right clicking on a flagged cell
    game.right_click(click_location)
    assert cell.state == 'hidden'
    assert game.flag_count == 0

    # Test right clicking on a revealed cell
    cell.state = 'revealed'
    game.right_click(click_location)
    assert cell.state == 'revealed'
    assert game.flag_count == 0
