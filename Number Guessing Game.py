"""
day-12-1-exercise
guess-the-number-final
"""
import random

logo = '''

  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ` _ \| '_ \ / _ \ '__|
/ /_\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|  
'''
NUMBER = random.randint(1, 100)

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print(f"Pssst, the correct answer is {NUMBER}")
difficulty = input("Choose a difficulty. Type 'hard' or else:")
attempt = 5 if difficulty == 'hard' else 10


def attempts(attempt):
    print(f"You have {attempt} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == NUMBER:
        print(f"You got it! The answer was {guess}.")
        return False, False
    elif guess > NUMBER:
        print("Too high.")
        if attempt > 1:
            print("Guess again.")
        return attempt - 1, True
    elif guess < NUMBER:
        print("Too low.")
        if attempt > 1:
            print("Guess again.")
        return attempt - 1, True

while attempt:
    attempt, lose = attempts(attempt)

if lose:
    print("You've run out of guesses, you lose.")

# while attempt:
#     print(f"You have {attempt} attempts remaining to guess the number.")
#     guess = int(input("Make a guess: "))
#     if guess == NUMBER:
#         print(f"You got it! The answer was {guess}.")
#         attempt = False
#     elif guess > NUMBER:
#         print("Too high.")
#         print("Guess again.")
#         attempt -= 1
#     elif guess < NUMBER:
#         print("Too low.")
#         print("Guess again.")
#         attempt -= 1
# else:
#     print("You've run out of guesses, you lose.")
