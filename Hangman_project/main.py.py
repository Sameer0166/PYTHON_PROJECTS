import random
from hangman_art import*
from hangman_words import words_list
print(logo)
lives=6
guess=random.choice(words_list)
place=""
print("Guess the letter:",end="")
for placeholder in guess:
    place+="_"
    print("_",end="")
print(stages[lives])
game_over=False
correct_letter=[]
while not game_over:
    print(f"********************{lives}/6 LIVES LEFT********************")
    user_input= input("enter your choice:").lower()
    if user_input in guess and user_input not in correct_letter:
        correct_letter.append(user_input)
    if user_input in guess:
        print("You guessed the word")
    display = ""
    if user_input in correct_letter:
        print(f"You already guessed {user_input}")
    for letter in guess:
        if letter in correct_letter:
            display += letter
        else:
            display+="_"
    print(display)

    if user_input not in guess:
        lives-=1
        print(f"You have guessed {user_input},that's not in the word,you have {lives} lives left")
        if lives==0:
            game_over=True
            print("********************YOU LOOSE********************")
    print(stages[lives])
    if "_" not in display:
        game_over=True
        print("You win!")
print("The word was:",guess)