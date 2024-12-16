import random

def playgame():
    def deal_cards():
        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
        card = random.choice(cards)
        return card

    def calculate_score(cards):
        if sum(cards) == 21 and len(cards) == 2:
            return 0
        if 11 in cards and sum(cards) > 21:
            cards.remove(11)
            cards.append(1)
        return sum(cards)

    def compare(user_score, computer_score):
        if user_score == computer_score:
            return "draw"
        elif computer_score == 0:
            return "You lose, Opponent has a blackjack"
        elif user_score == 0:
            return "You win"
        elif user_score > 21:
            return  "you lose, You went over"
        elif computer_score > 21:
            return "you win, Opponent went over"
        elif user_score < 21 and user_score > computer_score:
            return "you win"
        elif computer_score < 21 and user_score < computer_score:
            return "You lose"
        else:
            return "error"

    user_cards= []
    computer_cards = []
    computer_score = -1
    user_score = -1
    isgameover = False

    for _ in range(2):
        user_cards.append(deal_cards())
        computer_cards.append(deal_cards())


    # def cont():
    #     user_cards.append(deal_cards())
    #     user_score = calculate_score(user_cards)
    #     print(f"your cards:{user_cards}. Your score: {user_score}")
    #     print(f"Computer Cards:{user_cards[0]}.")
    #
    def final():

        print(f"your final cards:{user_cards}. Your final score: {user_score}")
        print(f"Computer final Cards:{user_cards}. Computer final score {computer_score}")

    while isgameover is False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"your cards:{user_cards}. Your score: {user_score}")
        print(f"Computer Cards:{user_cards[0]}.")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            isgameover = True

        else:
            choice = input("Type 'y' to get another card, Type 'n' to pass ")
            if choice == "y":
                user_cards.append(deal_cards())
            else:
                isgameover = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"your final cards:{user_cards}. Your final score: {user_score}")
    print(f"Computer final Cards:{user_cards}. Computer final score {computer_score}")
    print(compare(user_score, computer_score))

while input("do you want to play a game of blackjack?? 'y' or 'n': ") == "y":
    playgame()


