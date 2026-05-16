import random
should_continue = True
while should_continue:
    user_input = input("Do you want to play the Blackjack game? (y/n): ")
    if user_input == "y":
        should_continue = True
        def cards():
            list_of_cards = [11,2,3,4,5,6,7,8,9,10,10,10,10,10]
            card1=random.choices(list_of_cards)#same logic for adding the two random choices of cards to check total>21
            card2=random.choices(list_of_cards)
            card3=random.choices(list_of_cards)
            card4=random.choices(list_of_cards)
            dealer_card=card3+card4
            print("Dealers cards are:", dealer_card[0])
            your_card=card1+card2
            print("Your_card is:",your_card)
            user_choice = input("Type 'y' to get another card and 'n' for pass ")
            if user_choice == "y":
                card5=random.choices(list_of_cards)+card1+card2
                your_card=card5
                print("Your cards are:",your_card)
            elif user_choice == "n":
                card6 = random.choices(list_of_cards) + card4
                print("dealer's cards are:", card6)
                print("Dealers cards are:", dealer_card,)
        cards()
        def calculate_score(cards):
            return sum()

    elif user_input == "n":
        should_continue = False
        print("Thank you for not playing Blackjack game.\nGame Over")
        exit()