import pytest

from day2.main import open_game, calculate_score, calculate_best_move


def test_open_game():
    assert open_game('test.txt') == [['A', 'Y'], ['B', 'X'], ['C', 'Z']]


def test_calculate_score():
    games = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    assert calculate_score(games) == 15


def test_calculate_bext_move():
    games = [['A', 'Y'], ['B', 'X'], ['C', 'Z']]
    assert calculate_best_move(games) == 12