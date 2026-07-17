```text
             *               .                   *               *       /\   *   ____---_
                ___  *           .          .           *           ____---------/
 \  /\      *  /___\           *                      *     /\   __/
  \_____       (° o)   /\ /\/\      .          .      /\/\  ____/  ________
        \..._ (  :  ) ...._____           .    ____...-----/               \
             (   :   )         \_________...._/                             ......_____
~~________~~_____~~___~~~~~~______~~~~__~~~__~~___~~___~~~~~~___~~~~~~~__~~~~~~_____~~___~~ 
 /"       )(\"   \|"  \    /    " \  |"  |/  \|  "||"  \    /"  |     /""\    (\"   \|"  \  
(:   \___/ |.\\   \    |  // ____  \ |'  /    \:  | \   \  //   |    /    \   |.\\   \    | 
 \___  \   |: \.   \\  | /  /    ) :)|: /'        | /\\  \/.    |   /' /\  \  |: \.   \\  | 
  __/  \\  |.  \    \. |(: (____/ //  \//  /\'    ||: \.        |  //  __'  \ |.  \    \. | 
 /" \   :) |    \    \ | \        /   /   /  \\   ||.  \    /:  | /   /  \\  \|    \    \ | 
(_______/   \___|\____\)  \"_____/   |___/    \___||___|\__/|___|(___/    \___)\___|\____\) 
                                                                                            
                           .  . .-. .   .-. .-. .-. . . . . .         
                           |\/| |-  |    |  |  )| | | | | |\|         
                           :  ` `-' `-'  :  `-' `-' `.'.' ' :         
                           :             .            |    :
                                                      : 
```

# Snowman Meltdown

An interactive, Hangman-style word puzzle game for the terminal, written in Python. Save the snowman from melting by guessing the secret word letter by letter!

## Features

* **Charming ASCII Art:** A detailed, 10-stage snowman melting animation.
* **Robust Input Validation:** Protected against invalid characters, numbers, and accidental multi-letter inputs.
* **Play-Again Loop:** Start a new game instantly without having to restart the script.
* **Clean Code Architecture:** Fully modularized and designed according to official **PEP 8 Guidelines**.

---

## Installation & Quick Start

This game requires **Python 3.9 or newer** installed on your system.

1. **Clone the repository:**
   ```bash
    git clone https://github.com/Dni-schaf/Snowman-Meltdown.git
    cd Snowman-Meltdown
   
2. **Run the game:**
   ```bash
    python main.py


---
## Project Structure

The project is cleanly separated into specialized modules to keep the logic, UI, and data decoupled:

   - **main.py** – The entry point of the application, managing the main game loop (Play-Again).

   - **game_logic.py** – The core game mechanics (mistake tracking, validation, round handling).

   - **word_lib.py** – The word library containing the secret words.

   - **ascii_art.py** – The visual assets for the melting stages of the snowman.

---
## What I Learned

This project was a major milestone in my Python journey. While building it, I deepened my understanding of several core concepts:

   - **Set Theory in Python:** Instead of nested loops, I utilized Python's efficient .issubset() method to determine if the word has been fully guessed.

   - **Input Validation:** Implementing .isalpha() and string length checks to gracefully handle invalid user inputs.

   - **Modularization (Clean Code):** Breaking down code into specialized files to improve readability and maintainability.

   - **Type Hinting:** Applying type annotations (-> str, list[str]) for cleaner, self-documenting code.

---
## Credits

* Big header font generated with [Patorjk's ASCII Art Generator](https://patorjk.com/) (using the 'Merlin1' and 'AMC 3 Line' fonts).

---
## License

This project is licensed under the MIT License – feel free to modify, share, or use it as inspiration for your own projects!
</br>MIT — see [LICENSE](LICENSE).