# cli-number-guess

A command-line number-guessing game. The program picks a secret number, and
the player guesses until they win or run out of attempts. After each guess,
the game indicates whether the guess was too high or too low.

## Install

```powershell
python -m pip install -e .
```

## Run

```powershell
python -m cli_number_guess
```

## Test

```powershell
python -m pip install -e ".[test]"
python -m pytest
```
