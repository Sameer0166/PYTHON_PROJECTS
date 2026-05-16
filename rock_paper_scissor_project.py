import random
print("Welcome to Rock Paper Scissor Game")
rock = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
user = int(input("Enter 0:Rock\n1:Paper\n2:Scissor\nUser choice: "))
if user == 0:
    print(rock)
elif user == 1:
    print(paper)
elif user == 2:
    print(scissors)
else:
    print("Invalid input")
    exit()   # Stops the program here
computer = random.randint(0, 2)
print("Computer choice is:", computer)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)
if user == computer:
    print("It's a Draw")
elif user == 0 and computer == 2:
    print("User won")
elif user == 1 and computer == 0:
    print("User won")
elif user == 2 and computer == 1:
    print("User won")
else:
    print("Computer won")