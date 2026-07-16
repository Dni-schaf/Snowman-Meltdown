from urllib.parse import uses_relative

import game_logic


def main():
    while True:
        game_logic.play_game()
        user_input = input("\nTry again? (q for quit))").lower().strip()
        if user_input == "q":
            print("\nThanks for playing ☃️ Meltdown! See you next time!")
            break





if __name__ == "__main__":
    main()
