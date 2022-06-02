import os
import random

logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""

#Deal:
#both dealer and player get 2 cards each
#1 card of dealer is hidden
#if player gets 21 it's automatic blackjack, player wins unless dealer also has 21
#in which case it's a tie

#player gets to hit (get another card)
#or stand

#once player stands
#dealer reveals his card

carddeck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] 
#first 11 is ace which can be changed to 1, last three 10's are jack, queen and king

def eleven_to_ace(deck):
    for i in range(len(deck)):
        if deck[i] == 11:
            deck[i] = 1
            break
    return deck

def cardpicker():
    return random.choice(carddeck)

def deal():
    deck = [cardpicker(), cardpicker()]
    if deck == [11, 11]:
        deck = [11, 1]
    return deck

def hit(deck):
    return deck.append(cardpicker())

def dealers_play(deck):
    if sum(deck) < 17:
        deck.append(cardpicker())
        dealers_play(deck)
    return deck

def show_current_position(player_deck, dealer_deck):
    print(f"Your cards: {player_deck}, current score: {sum(player_deck)}")
    print(f"Dealer's first card: {dealer_deck[0]}\n")

def show_final_position(player_deck, dealer_deck):
    print(f"Your final hand is: {player_deck}, final score: {sum(player_deck)}")
    print(f"Dealer's final hand is: {dealer_deck}, final score: {sum(dealer_deck)}\n")

def check_win(player_deck, dealer_deck):
    if sum(player_deck) > 21:
        print("You lose!\n")
    elif sum(dealer_deck) <= 21 and sum(dealer_deck) > sum(player_deck):
        print("You lose!\n")
    elif sum(dealer_deck) > 21 and sum(player_deck) <= 21:
        print("You win!\n")
    elif sum(dealer_deck) < sum(player_deck):
        print("You win!\n")
    else:
        print("It's a tie!\n")






game_on = True

while game_on:
    user_input = input("Would you like to play a game of BlackJack (y or n): ")
    if user_input == 'n':
        game_on = False
    else:
        os.system('cls')
        outcome = False

        print(logo)

        dealer = deal()
        player = deal()

        show_current_position(player, dealer)

        if sum(player) == 21:
            show_final_position(player, dealer)
            check_win(player, dealer)
            outcome = True

        while outcome == False and sum(player) < 21:
            user_hit = input("Would you like to hit (y) or stand (n): ")
            if user_hit == 'y':
                hit(player)
                if sum(player) > 21:
                    eleven_to_ace(player)
                show_current_position(player, dealer)
            else:
                break

        if outcome == False:
            dealers_play(dealer)
            show_final_position(player, dealer)
            check_win(player, dealer)
            outcome = True

        
