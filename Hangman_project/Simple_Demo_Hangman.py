print("Welcome to Hangman Game🎮\nLet's save the person from Hanging")
import random
word_list=['sameer','sabeel','akanksha','yasmeen']
for word in word_list:
    print(word)
chosen_word=random.choice(word_list)
while True:
    user_input=input("Guess the name:")
    if user_input not in word_list:
        print("You have entered out of the list of words\nplease try again and enter the names present in the wordlist:")
    elif user_input in word_list and user_input==chosen_word:
        print(f"You guessed correctly, You won!\n The guessed word is {user_input} and the chosen word is also:",chosen_word)
        break
    else:
        print("Sorry, you lost!\nThe chosen word is:",chosen_word)
        break