
import random

words = ["python", "coding", "intern", "github", "laptop"]
word = random.choice(words)
guessed = []
attempts = 6

while attempts > 0:
    display = " ".join(c if c in guessed else "_" for c in word)
    print("\nWord:", display)
    if "_" not in display:
        print("🎉 You won!")
        break
    letter = input("Guess a letter: ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Enter a single letter.")
    elif letter in guessed:
        print("Already guessed.")
    else:
        guessed.append(letter)
        if letter not in word:
            attempts -= 1
            print(f"Wrong! Attempts left: {attempts}")
else:
    print("Game over! Word was:", word)