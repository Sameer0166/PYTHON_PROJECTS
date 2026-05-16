print("welcome to Treasure Island🤑\n Your mission is to find the treasure")
print('''  ____________________________________________________________________
 / \-----     ---------  -----------     -------------- ------    ----\
 \_/__________________________________________________________________/
 |~ ~~ ~~~ ~ ~ ~~~ ~ _____.----------._ ~~~  ~~~~ ~~   ~~  ~~~~~ ~~~~|
 |  _   ~~ ~~ __,---'_       "         `. ~~~ _,--.  ~~~~ __,---.  ~~|
 | | \___ ~~ /      ( )   "          "   `-.,' (') \~~ ~ (  / _\ \~~ |
 |  \    \__/_   __(( _)_      (    "   "     (_\_) \___~ `-.___,'  ~|
 |~~ \     (  )_(__)_|( ))  "   ))          "   |    "  \ ~~ ~~~ _ ~~|
 |  ~ \__ (( _( (  ))  ) _)    ((     \\//    " |   "    \_____,' | ~|
 |~~ ~   \  ( ))(_)(_)_)|  "    ))    //\\ " __,---._  "  "   "  /~~~|
 |    ~~~ |(_ _)| | |   |   "  (   "      ,-'~~~ ~~~ `-.   ___  /~ ~ |
 | ~~     |  |  |   |   _,--- ,--. _  "  (~~  ~~~~  ~~~ ) /___\ \~~ ~|
 |  ~ ~~ /   |      _,----._,'`--'\.`-._  `._~~_~__~_,-'  |H__|  \ ~~|
 |~~    / "     _,-' / `\ ,' / _'  \`.---.._          __        " \~ |
 | ~~~ / /   .-' , / ' _,'_  -  _ '- _`._ `.`-._    _/- `--.   " " \~|
 |  ~ / / _-- `---,~.-' __   --  _,---.  `-._   _,-'- / ` \ \_   " |~|
 | ~ | | -- _    /~/  `-_- _  _,' '  \ \_`-._,-'  / --   \  - \_   / |
 |~~ | \ -      /~~| "     ,-'_ /-  `_ ._`._`-...._____...._,--'  /~~|
 | ~~\  \_ /   /~~/    ___  `---  ---  - - ' ,--.     ___        |~ ~|
 |~   \      ,'~~|  " (o o)   "         " " |~~~ \_,-' ~ `.     ,'~~ |
 | ~~ ~|__,-'~~~~~\    \"/      "  "   "    /~ ~~   O ~ ~~`-.__/~ ~~~|
 |~~~ ~~~  ~~~~~~~~`.______________________/ ~~~    |   ~~~ ~~ ~ ~~~~|
 |____~jrei~__~_______~~_~____~~_____~~___~_~~___~\_|_/ ~_____~___~__|
 / \----- ----- ------------  ------- ----- -------  --------  -------\
 \_/__________________________________________________________________/''')
print("choose the path to go left or right to reach the treasure🛣️")
path1=input('Now you are at the cross road.which side of the road do you want to cross to reach the treasure "left" or "right"?').lower()
if path1=='right':
    print('Oops!Fell into a hole,it\'s a dead end 😥\nGame over💔\n Better luck next time🤗')
elif path1=='left':
    path2=input('Now you are the river, do you want to "swim" or "wait" until the boat comes to the river side🤔?').lower()
    if path2=='swim':
        print('Oops!attacked by trout😰\n Game over💔\nBetter luck next time 🤗')
    elif path2=='wait':
            path3=input("Hurray!Let's Go🥳 Now you are the final stage after crossing the river\nselect any of this door you want to go to reach the treasure?\n1.Red\n2.Yellow\n3.Blue\nEnter the door name:").lower()
            if path3=='red':
                print("Oops you have entered the wrong door\n Burned by fire🐦‍🔥\nTreasure not found😔\n Game over💔\nBetter luck next time🤗")
            elif path3=='yellow':
                print("spell the magic code to open")
                print("Hint:I am not a mouth, but I open wide. I have hinges but no wings. I have a handle you turn, and I protect your house from the outside. What am I?")
                user = input("spell the magic code to open the door in sanskrit:").lower()
                if user=="kapatam udghataya" or user=="dvaram udghataya"or user=="dvaram udghatayatu":
                    print("Bravery🏴‍☠️You have won the Treasure🪙\nYou Win!🤑")
                    print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
*******************************************************************************

''')
                else:
                    print("Treasure had lot due to misspelled magic code and you lost it sorry😔 \n Better luck next time🤗 ")
            elif path3=='blue':
                print("Oops!Eaten by beasts.😬\nGame Over💔\nBetter luck next time🤗")
else:
    print("wrong choice!")