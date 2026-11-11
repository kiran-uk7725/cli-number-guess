import random
from cli_number_guess.utils.records import load_records, save_records
from dataclasses import dataclass
from pathlib import Path
import sys

@dataclass(frozen=True)
class Difficulty:
    """One game difficulty level."""
    name: str
    upper_bound: int
    max_attempts: int

difficulties_list = [Difficulty(name="easy", upper_bound=10, max_attempts=5), Difficulty(name="medium", upper_bound=50, max_attempts=7), Difficulty(name="hard", upper_bound=100, max_attempts=10)]

DIFFICULTIES: dict[str, Difficulty] = {difficulty.name: difficulty for difficulty in difficulties_list}


def get_valid_int(prompt: str, low: int, high: int) -> int:
    """Prompt until the user enters a whole number within the inclusive range.

    Args:
        prompt: Text displayed before reading the user's input.
        low: Smallest accepted integer.
        high: Largest accepted integer.

    Returns:
        The validated integer entered by the user.
    """
    while True:
        try:
            user_input = int(input(prompt).strip())
            if not low <= user_input <= high:
                raise ValueError
            return user_input
        except ValueError:
            print(f"Please enter a whole number between {low} and {high}.")

def choose_difficulty(difficulty_map: dict[str, Difficulty]) -> Difficulty:
    """Prompt the user to select a difficulty from the available options.

    Args:
        difficulty_map: Mapping from difficulty names to their game settings.

    Returns:
        The settings associated with the selected difficulty.
    """
    while True:
        difficulty = input("\nChoose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty not in difficulty_map:
            print("please choose from given difficulties!")
            continue
        return difficulty_map[difficulty]

def play_round(upper_bound: int, max_attempts: int) -> int | None:
    """Run one number-guessing round using the given limits.

    Args:
        upper_bound: Largest possible secret number and accepted guess.
        max_attempts: Maximum number of guesses allowed.

    Returns:
        The number of guesses used if the player wins, or ``None`` if
        the player uses all allowed attempts without guessing correctly.
    """
    secret = random.randint(1, upper_bound)
    user_attempts = 1

    while user_attempts <= max_attempts:
        user_input = get_valid_int(f"\nAttempt {user_attempts}/{max_attempts} - your guess: ", low=1, high=upper_bound)

        if user_input == secret:
            print(f"Correct! You got it in {user_attempts} attempt{'s' if user_attempts != 1 else ''} 🎉")
            return user_attempts

        if user_input < secret:
            print("Too low!")
        elif user_input > secret:
            print("Too high!")

        user_attempts += 1
    print(f"\nThe secret number was {secret}. Better luck next time 🤞")
    return None

def play_again() -> bool:
    """Ask whether the user wants to play another round.

    Returns:
        ``True`` if the user chooses yes, otherwise ``False``.
    """
    while True:
        answer = input("\nPlay again? (Y/n): ").strip().lower()

        if answer in ("yes", "y"):
            return True
        elif answer in ("no", "n"):
            return False
        else:
            print("Invalid input. Please enter 'y' or 'n'.")

def display_bestscore(records: dict[str, int]) -> None:
    """Print the best recorded winning attempt count for each difficulty.

    Args:
        records: Mapping from difficulty names to their fewest winning
            attempt counts.
    """
    if not records:
        print("No best scores yet.")
        return

    print("\nBest scores (fewest attempts):")
    for difficulty in DIFFICULTIES:
        if difficulty in records:
            attempts = records[difficulty]
            print(f"{difficulty.capitalize()}: {attempts} attempt{'s' if attempts != 1 else ''}")

def main():
    """Run the game loop and keep best scores for the current session."""
    records_loc = Path()
    records = load_records()

    while True:
        try:
            difficulty = choose_difficulty(DIFFICULTIES)
            print(f"I'm thinking of a number between 1 and {difficulty.upper_bound} 🤔 You have {difficulty.max_attempts} attempts 😁")
            attempts = play_round(difficulty.upper_bound, difficulty.max_attempts)
            if attempts is not None:
                records[difficulty.name] = min(records.get(difficulty.name, attempts), attempts)
                display_bestscore(records)

            if not play_again():
                print("\nThanks for playing 😊")
                break

        except (KeyboardInterrupt, EOFError):
            print("\nHave a good day 😀")
            sys.exit(0)

if __name__ == "__main__":
    main()

