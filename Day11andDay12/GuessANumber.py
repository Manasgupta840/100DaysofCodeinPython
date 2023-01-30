logo = """
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
"""
print(logo)
import random

system_choice = random.randint(1, 100)


def game(a):
    if (a == 0):
        print(f"You lose, the number is {system_choice}")
        return
    print(f"You have {a} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if (guess > system_choice):
        print("Too high.")
    elif (guess < system_choice):
        print("Too low.")
    else:
        print(f"wooo. You got it the number is {system_choice}")
        return
    a = a - 1
    game(a)


print("Welcome to the number Guessing Game! ")
print("I'm thinking of a number between 1 and 100. ")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
if (difficulty == "easy"):
    game(10)
elif (difficulty == "hard"):
    game(5)
else:
    print("please choose the valid option")
