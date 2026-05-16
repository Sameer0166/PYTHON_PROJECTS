import random

# Cards in Blackjack
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


# Deal one random card
def deal_card():
    return random.choice(cards)


# Calculate total score
def calculate_score(card_list):

    total = sum(card_list)

    # Blackjack condition
    if total == 21 and len(card_list) == 2:
        return 0

    # Ace handling
    while total > 21 and 11 in card_list:
        ace_index = card_list.index(11)
        card_list[ace_index] = 1
        total = sum(card_list)

    return total


# Compare scores and decide winner
def compare(player_score, dealer_score):

    if player_score == dealer_score:
        return "Draw"

    elif dealer_score == 0:
        return "Dealer has Blackjack. You lose."

    elif player_score == 0:
        return "Blackjack! You win."

    elif player_score > 21:
        return "You went over 21. You lose."

    elif dealer_score > 21:
        return "Dealer went over 21. You win."

    elif player_score > dealer_score:
        return "You win."

    else:
        return "Dealer wins."


# Main game function
def play_game():

    player_cards = []
    dealer_cards = []

    # Initial 2 cards
    for _ in range(2):
        player_cards.append(deal_card())
        dealer_cards.append(deal_card())

    game_over = False

    while not game_over:

        player_score = calculate_score(player_cards)
        dealer_score = calculate_score(dealer_cards)

        print("\nYour cards:", player_cards)
        print("Your score:", player_score)

        print("Dealer first card:", dealer_cards[0])

        # Check blackjack or bust
        if player_score == 0 or dealer_score == 0 or player_score > 21:
            game_over = True

        else:
            user_choice = input("Type 'y' to Hit or 'n' to Stand: ")

            if user_choice == "y":
                player_cards.append(deal_card())

            else:
                game_over = True

    # Dealer turn
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    # Final results
    print("\nFINAL RESULT")
    print("Your cards:", player_cards)
    print("Your final score:", player_score)

    print("Dealer cards:", dealer_cards)
    print("Dealer final score:", dealer_score)

    print(compare(player_score, dealer_score))


# Game loop
while True:

    start = input("\nDo you want to play Blackjack? (y/n): ")

    if start == "y":
        play_game()

    else:
        print("Game ended.")
        break