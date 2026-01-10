# Hangman Game

A classic word-guessing game implemented in Python. Test your vocabulary skills by guessing letters to reveal a hidden word before the hangman is complete!

## Features

- Interactive command-line interface
- ASCII art hangman stages
- Random word selection from a curated list
- Input validation and feedback
- Win/lose conditions with appropriate messages

## Requirements

- Python 3.6 or higher

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/gatchez/hangman-game.git
   ```
2. Navigate to the project directory:
   ```bash
   cd hangman-game
   ```

## Usage

Run the game using:
```bash
python hangman_game.py
```

## How to Play

1. The game will display a series of underscores representing the letters of a hidden word.
2. Guess one letter at a time by typing it and pressing Enter.
3. If the letter is in the word, it will be revealed in its correct positions.
4. If the letter is not in the word, you'll lose a life and the hangman drawing will progress.
5. You have 6 lives to guess the word correctly.
6. Win by guessing all letters before running out of lives, or lose when the hangman is complete.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.