from src.gameClass import Game
import pytest

@pytest.fixture()
def game():
    g = Game()
    return g
