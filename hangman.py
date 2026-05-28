import random

# List of words
words = ["python", "computer", "internship", "programming", "codealpha"]

# Randomly choose a word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of attempts
tries = 6

# Simple hint system
if word == "python":
    hint = "A popular programming language"
elif word == "computer":
    hint = "An electronic device"
elif word == "internship":
    hint = "A training program for students"
elif word == "programming":
    hint = "Writing code"
else:
    hint = "Related to Code Alpha"

# Hangman stages
hangman_stages = [
    """
       -----
       |   |
           |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

print("🎮 Welcome to Hangman Game!")
print("💡 Hint:", hint)

# Game loop
while tries > 0:

    print(hangman_stages[6 - tries])

    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Win condition
    if "_" not in display_word:
        print("🎉 Congratulations! You guessed the word:", word)
        break

    guess = input("Enter a letter: ").lower()

    # Already guessed check
    if guess in guessed_letters:
        print("⚠️ Already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Wrong guess
    if guess not in word:
        tries -= 1
        print("❌ Wrong guess!")
        print("Remaining tries:", tries)

# Game over
if tries == 0:
    print(hangman_stages[6])
    print("\n💀 Game Over!")
    print("The word was:", word)