import random

# Define card values and suits
card_values = {
    '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10,
    'J': 10, 'Q': 10, 'K': 10, 'A': 11
}
suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']

# Function to create and shuffle a deck of cards
def create_deck():
    deck = []
    for suit in suits:
        for value in card_values.keys():
            deck.append((value, suit))
    random.shuffle(deck)
    return deck

# Function to calculate the total value of a hand
def calculate_hand_value(hand):
    value = 0
    num_aces = 0
    for card in hand:
        value += card_values[card[0]]
        if card[0] == 'A':
            num_aces += 1
    while value > 21 and num_aces > 0:
        value -= 10
        num_aces -= 1
    return value

# Function to display a hand
def display_hand(hand, name):
    print(f"{name}'s hand: {', '.join([f'{card[0]} of {card[1]}' for card in hand])}")

# Main game function
def play_blackjack():
    deck = create_deck()
    
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]
    
    display_hand(player_hand, "Player")
    display_hand(dealer_hand[:1], "Dealer")
    
    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)
    
    while player_value < 21:
        action = input("Do you want to (H)it or (S)tand? ").upper()
        if action == 'H':
            player_hand.append(deck.pop())
            display_hand(player_hand, "Player")
            player_value = calculate_hand_value(player_hand)
        elif action == 'S':
            break
    
    if player_value > 21:
        print("Player busts! Dealer wins.")
        return
    
    while dealer_value < 17:
        dealer_hand.append(deck.pop())
        dealer_value = calculate_hand_value(dealer_hand)
    
    display_hand(dealer_hand, "Dealer")
    
    if dealer_value > 21 or player_value > dealer_value:
        print("Player wins!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

# Run the game
if __name__ == "__main__":
    play_blackjack()
