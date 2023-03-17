# import necessary modules and classes
import pytest
from main import Game

# define a fixture to create a new Game object with beginner difficulty
@pytest.fixture
def new_game():
    game = Game()
    game.set_difficulty('beginner')
    return game

def test_update_clues(new_game):
    # place mines in the corners of the board to create clues
    new_game.cells[(0, 0)].has_mine = True
    new_game.cells[(0, 1)].has_mine = True
    new_game.cells[(1, 0)].has_mine = True

    # update the clues
    new_game.update_clues()

    # check if the clues were updated correctly
    assert new_game.cells[(0, 0)].clue == 2
    assert new_game.cells[(0, 1)].clue == 2
    assert new_game.cells[(1, 0)].clue == 2
    assert new_game.cells[(1, 1)].clue == 3
