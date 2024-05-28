import random

def deal_card():
    """Return a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def cal_score(cards):
    """Calculate the score based on the cards in hand."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if sum(cards) > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        
    return sum(cards)

def compare(user_score, computer_score):
    """Compare the scores of the user and the computer to determine the outcome."""
    if user_score == computer_score:
        return "Draw"
    elif user_score == 0:
        return "Win with a Blackjack"
    elif computer_score == 0:
        return "Lose, Opponent has a Blackjack"
    elif user_score > 21:
        return "You went over, You Lose"
    elif computer_score > 21:
        return "Opponent went over, You Win"
    elif user_score > computer_score:
        return "You Win"
    else:
        return "You Lose"

# Start the game
while True:  # Run the game endlessly
    user_cards = []
    computer_cards = []
    is_game_over = False

    # Deal initial cards
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        # Calculate scores
        user_score = cal_score(user_cards)
        computer_score = cal_score(computer_cards)

        # Display current hands and scores
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's First Card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            # Ask the user for their move
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Let the computer play
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = cal_score(computer_cards)

    # Display final hands and scores
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

    # Ask the user if they want to play again
    play_again = input("Do you want to play again? Type 'y' to play or 'n' to quit: ")
    if play_again != 'y':
        break  # End the game loop if the user doesn't want to play again
