import random
import ascii_art
import word_lib

"""
This controls a round of the game. It validates user input, 
saves the entries, and provides feedback. 
`max_guesses` specifies how many incorrect letters the player 
is allowed to enter before the game ends.
"""

MAX_GUESSES = 10  #must match ascii_art.STAGES - 1


def get_random_word() -> str:
    """Selects a random word from the list."""
    return random.choice(word_lib.WORDS)


def display_game_state(mistakes: int, secret_word: str, guessed_letters: list[str]) -> None:
    """Print the current status of the snowman and the word to the screen."""
    print(ascii_art.STAGES[mistakes])
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print(f"Word: {display_word}\n")


def valid_guess(guess: str) -> bool:
    """Checks if guess is valid."""
    return len(guess) == 1 and guess.isalpha()


def play_game():
    """Runs a single round of Snowman Meltdown from start to finish."""
    secret_word = get_random_word()
    guessed_letters = []
    mistakes = 0

    print("Welcome to Snowman Meltdown!")
    display_game_state(mistakes, secret_word, guessed_letters)

    while mistakes < MAX_GUESSES:
        guess = input("Guess a letter: ").lower()
        while not valid_guess(guess):
            guess = input("Invalid input! Please enter exactly one letter: ").lower()
        guessed_letters.append(guess)
        if guess not in secret_word:
            mistakes += 1

        display_game_state(mistakes, secret_word, guessed_letters)

        if set(secret_word).issubset(set(guessed_letters)):
            print("Congratulations, you saved the snowman!")
            break
    else:
        print(f"Game Over! The word was: {secret_word}")
