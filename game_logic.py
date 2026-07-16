import random
import ascii_art
import word_lib


MAX_GUESSES = 10


def get_random_word():
    """Selects a random word from the list."""
    return word_lib.WORDS[random.randint(0, len(word_lib.WORDS) - 1)]


def display_game_state(mistakes, secret_word, guessed_letters):
    # Display the snowman stage for the current number of mistakes.
    print(ascii_art.STAGES[mistakes])
    # Build a display version of the secret word.
    display_word = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    print("Word: ", display_word)
    print("\n")


def valid_guess(guess):
    """Checks if guess is valid."""
    return len(guess) == 1 and guess.isalpha()


def play_game():
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
