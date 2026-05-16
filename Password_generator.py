import random
letters='abcdefghijklmnopqrstuvwxyz'
special_char='~','`','!','@','#','$','%','^','&','*','(',')','-','_','+'
numbers='1','2','3','4','5','6','7','8','9','0'

print("welcome to the password generator🔒")
user_letter=int(input("enter the no.of characters to generate password:"))
user_special_char=int(input("enter the no.of special character to generate password:"))
user_numbers=int(input("enter the no.of numbers to generate password:"))

password=""

for char in range(1,user_letter+1):
    password+=random.choice(letters)
for spe in range(1,user_special_char+1):
    password+=random.choice(special_char)
for num in range(1,user_letter+1):
    password+=random.choice(numbers)
print("Guess my password generated randomly.\nplay at your own risk😊\nType 'exit' to exit.")
user_input = input("Decode the password to open the gift:")
if user_input=='exit':
    print("Oops!you gave up😬,The generated password is:",password)
    exit()
elif user_input == password:
        print("use have won 100000000/-rs 🥳🥳🥳 ")
elif user_input != password:
        print("wrong password,Try again😁\n You can't win this game with me 😎")
print("The password is:",password)