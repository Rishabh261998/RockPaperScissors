from Computer import *
from Player import *
from RockPaperScissors import *


def test_get_computer_choice():
    """Function to test the get_choice method of Computer class"""
    computer = Computer()
    computer_choice = computer.get_choice()
    assert computer_choice in [1, 2, 3]


def test_get_game_winner():
    """Function to test the get_game_winner function of RockPaperScissors class"""
    game = RockPaperScissors()
    assert game.get_game_winner(1, 2) == -1
    assert game.get_game_winner(1, 3) == 1
    assert game.get_game_winner(2, 2) == 0
    assert game.get_game_winner(3, 1) == -1
    assert game.get_game_winner(0, 1) == -2


def test_get_player_choice(monkeypatch):
    """Function to test the get_choice function of Player class"""
    player = Player()
    monkeypatch.setattr('builtins.input', lambda _: 1)
    output = player.get_choice()
    assert output == 1


def test_get_playing(monkeypatch):
    """Function to test the get_playing function of RockPaperScissors class"""
    game = RockPaperScissors()
    monkeypatch.setattr('builtins.input', lambda _: 2)
    output = game.get_playing()
    assert output == 2


