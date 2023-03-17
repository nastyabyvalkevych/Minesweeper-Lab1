from main import *
import pytest

@pytest.fixture
def game():
    return Game()

def test_reveal_all_cells(game):
    game.reveal_all_cells()
    assert game.revealed_count == game.size['rows'] * game.size['cols']