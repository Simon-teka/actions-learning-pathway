import random

def display_hint(secret_word, user_guess):
    hint = []
    for i in range(len(secret_word)):
        if user_guess[i] == secret_word[i]:
            hint.append(user_guess[i].upper())
        elif user_guess[i] in secret_word:
            hint.append(user_guess[i].lower())
        else:
            hint.append("_")
    return " ".join(hint)

def main():
    print("Welcome to the word guessing game!")
    words = ["hello", "world", "python", "program", "game"]  # List of words to guess
    secret_word = random.choice(words)
    num_guesses = 0
    max_guesses = 5  # Limiting the number of guesses
    correct = False
    
    while not correct and num_guesses < max_guesses:  # Limiting the number of guesses
        print(f"Your hint is: {'_ ' * len(secret_word)}")
        guess = input("What is your guess? ").lower()
        num_guesses += 1
        
        if len(guess) != len(secret_word):
            print("Sorry, the guess must have the same number of letters as the secret word.")
        elif guess == secret_word:
            correct = True
            print(f"Congratulations! You guessed it!\nIt took you {num_guesses} guesses.")
        else:
            print(f"Your hint is: {display_hint(secret_word, guess)}")
    
    if not correct:
        print(f"Sorry, you ran out of guesses! The word was {secret_word}")

if __name__ == "__main__":
    main()
