# Akire Cormier, CIS261, Guessing Game
import random

def title():
    print("Guess the Number!")
    print()
    
def game(limit):
    number = random.randint(1, limit)
    print(f"Guess a number from 1 to {limit}\n.")
    count = 1
    guess = int(input("Answer:  "))
    
    while(guess != number):
        if guess < number:
            print("That's too low.")
            count += 1
        elif guess > number:
            print("That's too high.")
            count += 1
        guess = int(input("Guess again: "))
    print(f"You guess it in {count} tries. \n")
    
def main():
    title()
    again = "YES"
    while again.upper() == "YES":
        limit = int(input("Enter the limit:"))
        game(limit)
        again = input("Do you want to play again? (YES/NO)")
        print()
    print("See ya!")
    
if __name__ == "__main__":
    main()
    