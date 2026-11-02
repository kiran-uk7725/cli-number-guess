import random

DIFFICULTIES: dict[str, tuple[int, int]]= {
    "easy": (10, 5),
    "medium": (50, 7),
    "hard": (100, 7)
}


def choose_difficulty(difficulty_map):
    while True:
        difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
        if difficulty not in difficulty_map:
            print("please choose from given difficulties!\n")
            continue
        return difficulty_map[difficulty]

