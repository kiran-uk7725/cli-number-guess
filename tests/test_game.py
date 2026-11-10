import pytest
from cli_number_guess.game import get_valid_int, choose_difficulty, DIFFICULTIES

def test_choose_difficulty_loop_until_valid(monkeypatch):
    responses = iter(["super hard", "ez", "easy"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    result = choose_difficulty(DIFFICULTIES)

    assert result == DIFFICULTIES["easy"]


def test_get_valid_int_loop_until_valid(monkeypatch):
    responses = iter(["-10", "1000", "abc", "20"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    result = get_valid_int(f"Your guess: ", 1, 50)

    assert result == 20