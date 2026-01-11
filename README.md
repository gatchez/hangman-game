# Hangman Game

[![Python Version](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A classic word-guessing game implemented in Python. Challenge your vocabulary by guessing letters to reveal a hidden word before the hangman figure is complete!

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Usage](#usage)
- [Game Rules](#game-rules)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features

- **Interactive CLI Interface**: User-friendly command-line gameplay
- **ASCII Art Display**: Visual hangman stages for enhanced experience
- **Random Word Selection**: Curated word list for varied gameplay
- **Input Validation**: Robust error handling and user feedback
- **Win/Loss Conditions**: Clear game outcomes with appropriate messages
- **Zero Dependencies**: Built using Python standard library only

## Prerequisites

- Python 3.6 or higher
- Command-line interface (Terminal/PowerShell/Command Prompt)

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/gatchez/hangman-game.git
   ```

2. **Navigate to the project directory:**
   ```bash
   cd hangman-game
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
   > **Note:** This project uses only Python standard library modules, so no external packages are required.

## Usage

Launch the game by running:
```bash
python hangman_game.py
```

Follow the on-screen prompts to guess letters and play the game.

### Example Gameplay
```
Guess a letter: a
_ _ _ _ _

Guess a letter: p
_ p _ _ _

Guess a letter: l
_ p p l _

Guess a letter: e
_ p p l e
```

## Game Rules

1. **Objective**: Guess the hidden word by suggesting letters within 6 attempts.

2. **Gameplay**:
   - The game displays underscores representing each letter of the hidden word
   - Enter one letter at a time when prompted
   - Correct guesses reveal the letter in its correct positions
   - Incorrect guesses reduce your remaining lives and advance the hangman drawing

3. **Winning**: Reveal all letters before losing all 6 lives

4. **Losing**: The hangman drawing is completed before guessing the word

5. **Input Rules**:
   - Only single alphabetic characters are accepted
   - Guesses are case-insensitive
   - Previously guessed letters cannot be repeated

## Contributing

We welcome contributions to improve the Hangman Game! Here's how you can contribute:

### Development Setup
1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and test thoroughly
4. Commit your changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature/your-feature-name`
6. Open a Pull Request

### Guidelines
- Follow PEP 8 style guidelines
- Add comments for complex logic
- Test your changes thoroughly
- Update documentation as needed
- Ensure backward compatibility

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Collins**  
Copyright © 2026 Collins. All rights reserved.

---

*Enjoy playing Hangman! If you find any issues or have suggestions for improvements, please open an issue on GitHub.*