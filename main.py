import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_card():
    deal = random.choice(cards)
    return deal


def begin_game():
    print(logo)
    user_cards = []
    user_cards.append(deal_card())
    user_cards.append(deal_card())

    computer_cards = []
    computer_cards.append(deal_card())
    computer_cards.append(deal_card())

    game_over = False

    def calculate_score(lst):
        if 10 in lst and 11 in lst and len(lst) == 2:
            return 0
        else:
            total = sum(lst)
            if 11 in lst and total > 21:
                lst.remove(11)
                lst.append(1)
            return total

    def compare(user_scores, computer_scores):
        if user_score == computer_score:
            return "It's adraw"
        elif computer_score == 0 or user_score > 21:
            return "You lost"
        elif user_score == 0 or computer_score > 21:
            return "You won"
        elif computer_score > user_score:
            return "You lost"
        else:
            return"You won"

    while game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(
            f"Your cards are: {user_cards}. Your current score is: {user_score}")
        print(
            f"The computer's first card is : {computer_cards[0]}. ")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            draw_again = input(
                "Would you like to draw another card? Type 'yes' or 'no'")
            if draw_again == "yes":
                user_cards.append(deal_card())
            else:
                game_over = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(
        f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    restart = input("Type 'yes' to restart the game.")
    if restart == "yes":
        begin_game()


begin_game()
