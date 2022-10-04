import random as rnd
import TextArt as tx


def deal_card():
    """ Return a random card from the deck """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return rnd.choice(cards)


def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


def compare_score(user_score, dealer_score):
    # print(f"Dealer Score:")
    if user_score == dealer_score:
        tx.word_art("Draw")
        return "Draw!"
    elif dealer_score == 0:
        tx.word_art("Loose!")
        return "Loose! Opponent has BlackJack"
    elif user_score == 0:
        tx.word_art("Win!")
        return "Win with a BlackJack!"
    elif user_score > 21:
        tx.word_art("Loose!")
        return "You went over! You Loose!"
    elif dealer_score > 21:
        tx.word_art("Win!")
        return "Opponent went over! You Win!"
    elif user_score > dealer_score:
        tx.word_art("Win!")
        return "You Win!"
    else:
        tx.word_art("Loose!")
        return "You Loose!"


def play_game():
    user_cards = []
    dealer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        dealer_score = calculate_score(dealer_cards)
        print(f"User Cards: {user_cards} Current Score: {user_score}")
        print(f"Dealer First Card: {dealer_cards[0]}")

        if user_score == 0 or dealer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_choice = input("Type 'y' to get another card, type 'n' to pass: \n")
            if user_choice == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True
    while dealer_score != 0 and dealer_score < 17:
        dealer_cards.append(deal_card())
        dealer_score = calculate_score(dealer_cards)

    print(compare_score(user_score, dealer_score))
    print(f"Your Final Hand: {user_cards} Your Final Score: {user_score}")
    print(f"Dealer Final Hand: {dealer_cards} Dealer Final Score: {dealer_score} ")
    # tx.word_art_plain("----------")
    print("----------------")
    if input("Do You Want to Play Again: ") == 'y':
        print("\033[H\033[J", end="")
        play_game()
    else:
        print("Thank You For Playing!")
        tx.word_art("--OVER--")
