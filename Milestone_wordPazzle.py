
def main():
    print("Welcome to the word guessing game!")
    secret_word = "mosiah"
    num_guesses = 0
    correct = False
    
    while not correct:
        guess = input("What is your guess? ").lower()
        num_guesses += 1
        
        if guess == secret_word:
            correct = True
            print(f"Congratulations! You guessed it!\nIt took you {num_guesses} guesses.")
        else:
            print("Your guess was not correct.")

if __name__ == "__main__":
    main()