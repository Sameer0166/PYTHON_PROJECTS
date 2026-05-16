from art import logo
from random import randint
easy_level=10
hard_level=5

def check_answer(user_guess,actual_answer,turns):
    if user_guess>actual_answer:
        print("To High")
        return turns-1
    elif user_guess<actual_answer:
        print("To Low")
        return turns-1
    else:
        print(f"You got it!,The answer is {actual_answer}")
        return None

def set_difficulty():
    level=input("Choose the level of game 'easy' or 'hard': ")
    if level=="easy":
        return easy_level
    else:
        return hard_level

def game():
    print(logo)
    print("Welcome to the Number Guessing Game")
    print("I am thinking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"pssst,the correct answer is {answer}")

    turns=set_difficulty()


    guess=0
    while  guess!=answer:
        print(f"You have {turns} turns left to guess the number")
        guess=int(input("Make a guess: "))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you ran out of guesses,you lose")
            break
        elif guess!=answer:
            print("Guess again")
game()