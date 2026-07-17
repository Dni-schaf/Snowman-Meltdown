import game_logic

"""
Beschreibung aufbau porjekt
"""

def main():
    """Main entry point of the application running the game loop."""
    while True:
        game_logic.play_game()

        user_input = input("\nTry again? (q for quit)" ).lower().strip()
        if user_input == "q":
            print("\nThanks for playing ☃️ Meltdown! See you next time!")
            break


if __name__ == "__main__":
    main()
