import random
from hangman_stages import stages

# Expand the word list as needed
word_list = ["apple", "mango", "lemon"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
lives = 6


display = []
for _ in range(word_length):
    display += "_"
print(display)

end_of_game = False
while not end_of_game:

    guess = input("Guess a letter: ").lower()
    if guess in display:
        print(f"You have already guessed {guess}")
    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            if letter not in display:
                print("Bravo! You guessed correctly!")
            display[position] = letter
    print(display)

    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. You loose a life!")
        lives -= 1
        if lives == 0:
            print("You loose!")
            end_of_game = True
    if "_" not in display:
        # Join all elements in the list and turn it into a string.
        print(f"{''.join(display)} is the correct word. You win!")
        end_of_game = True 

# Print the ASCII art from 'stages' that corresponds to the current number if 'lives' the user has remaining.
    print(stages[lives])