import random

def guess_the_number():
    # Generate a random number between 1 and 50
    secret_number = random.randint(1, 50)

    print(" \n\tGUESS MY LUCKY NUMBER :)")
    name = input("\nEnter your name:")
    name_n = name.capitalize()
    txt = f'\n\tHello, {name_n} welcome to the game.\n  Guess your lucky number and win the prize!'
    print(txt)

    # Instructions for the game
    print("""
      
    GAME RULES :
     * Enter a number between 1 - 50
     * You have 3 chances to guess your lucky number.
      
      """)

    attempts = 0
    max_attempts = 3

    while attempts < max_attempts:
        user_guess = int(input("Your guess: "))
        attempts += 1

        if user_guess == secret_number:
            print(f"Congratulations! You guessed the correct number {secret_number} in {attempts} attempts.")
            break
        elif user_guess < secret_number:
            print("Too low! Try again.")
        elif user_guess > secret_number:
            print("Too high! Try again.")
    else:
        print(f"You lost! The correct number was {secret_number}.")
        
        
if __name__ == "__main__":
    guess_the_number()
        
        



