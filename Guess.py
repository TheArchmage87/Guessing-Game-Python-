import random
import time

def get_guess(level):
    while True:
        guess = input("Enter your guess: ")
        if guess.lower() == 'e':
            return guess
        try:
            return int(guess)
        except ValueError:
            print("Invalid input! Please enter an integer or 'e' to exit.")

def play_game():
    print("Welcome to the number guessing game!")
    print("You will start at level 1. For each level, you have to guess a counting number.")
    print("If your guess is close to the number, you'll see 'Close'.")
    print("If your guess is too low or too high, you'll see 'Too low!' or 'Too high!' respectively.")
    print("If you want to end the game, type 'e'.")
    print("Let's start the game!")

    level = 1

    while True:
        number_to_guess = random.randint(1, 100+(level-1)*10)
        print(f"Level {level}. Guess the number:")
        
        start_time = time.time()

        while True:
            guess = get_guess(level)
            if guess == 'e':
                print(f"You got to level {level}.")
                return
            if abs(guess - number_to_guess) <= 10+(level-1)*5:
                if guess != number_to_guess:
                    print("Close")
            else:
                if guess < number_to_guess:
                    print("Too low!")
                elif guess > number_to_guess:
                    print("Too high!")
            if guess == number_to_guess:
                break

        end_time = time.time()
        time_taken = end_time - start_time

        print(f"Congratulations! You finished {level}. It took you {time_taken} seconds.")
        
        level += 1

play_game()
