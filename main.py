import random
import sys

from replit import clear
from art import logo

def sum_calculate(player_cards):
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    if sum(player_cards) > 21 and 11 in player_cards:
        i = player_cards.index(11)
        player_cards[i] = 1
    summ = sum(player_cards)
    return summ

def print_current_hand(user_hand, computer_hand):
    print(f"Your cards: {user_hand}, current score {sum_calculate(user_hand)}")
    print(f"Computer's first card: {computer_hand[0]}")

def print_final_scores(user, computer):
    final_score_user = sum_calculate(user)
    final_score_computer = sum_calculate(computer)
    print(f"Your final hand: {user}, final score {final_score_user}")
    print(f"Computer's final hand: {computer}, final score {final_score_computer}")

def black_jack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    user_play = input("Play BlackJack? type y/n\n")

    while user_play.lower() == 'y':
        clear()
        print(logo)

        user_cards = [random.choice(cards), random.choice(cards)]
        computer_cards = [random.choice(cards), random.choice(cards)]

        computer_score = sum_calculate(computer_cards)
        user_score = sum_calculate(user_cards)

        while user_score < 21:
            print_current_hand(user_cards, computer_cards)
            if computer_score < 17:
                computer_cards.append(random.choice(cards))
                computer_score = sum_calculate(computer_cards)
            elif computer_score > 21:
                break

            add_one = input("Get one more? y to add another card, n to pass\n")

            if add_one == 'y':
                user_cards.append(random.choice(cards))
                user_score = sum_calculate(user_cards)
            else:
                break

        print_final_scores(user_cards, computer_cards)
        if user_score > 21 and computer_score > 21:
            print("Both lose, try again")
        elif user_score > 21 and computer_score <= 21:
            print('Oponent wins')
        elif computer_score > 21:
            print("You win")
        elif user_score == 21 and computer_score == 21:
            print('Try again')
        elif user_score == 21:
            print('You win')
        elif user_score > computer_score:
            print("You win")
        elif user_score == 0:
            print('Black Jack! You WIN')
        elif computer_score == 0:
            print('Black Jack! Oponent wins')
        else:
            print("Oponent wins")

        black_jack()
    print("exited")
    sys.exit()

black_jack()