import pytest
from game import choose_difficulty, DIFFICULTIES

def test_choose_difficulty_loop_until_valid(monkeypatch):
    responses = iter(["super hard", "ez", "easy"])
    monkeypatch.setattr("builtins.input", lambda _: next(responses))

    result = choose_difficulty(DIFFICULTIES)

    assert result == (10, 5)

