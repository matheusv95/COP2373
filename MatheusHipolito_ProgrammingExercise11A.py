import random

class Card:
    def __init__(self, suit, rank):
        self.suit = suit # The suit of the card
        self.rank = rank # The rank of the card

    def __str__(self):
        # Return a string representation of the card
        return f"{self.rank} of {self.suit}"

#Class to represent a deck of cards
class Deck:
    def __init__(self):
        #Create a deck with all cards
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]

    def shuffle(self):
        # Shuffle the deck to randomize the card order.
        random.shuffle(self.cards)

    def deal(self, num):
       dealt_cards = self.cards[:num]
       self.cards = self.cards[num:]
       return dealt_cards

# Function to show the cards in the player's hand.
def display_hand(hand):
    # Print each card with its position number (1, 2, 3, etc.)
    for i, card in enumerate(hand, start=1):
        print(f"{i}: {card}")

# Main function to control the game
def main():
    # Create a new deck and shuffle it
    deck = Deck()
    deck.shuffle()

    # Deal 5 cards to the player to create an initial hand
    hand = deck.deal(5)
    print("Your initial hand:")
    display_hand(hand)  # Show initial hand

    # Ask player which card they want to replace
    replace_input = input("Enter card positions to replace (e.g., 1, 3, 5), or press Enter to keep all: ")

    # If player enters positions, process the replacements
    if replace_input:
        positions = [int(pos) - 1 for pos in replace_input.split(',') if pos.strip().isdigit()]

        # Replace each selected card with a new one from the deck
        for pos in positions:
            if 0 <= pos < len(hand):  # Check that the position is valid
                hand[pos] = deck.deal(1)[0]  # Replace the card at the position

    # Show the final hand after replacements
    print("Your new hand:")
    display_hand(hand)

# Runs the program
if __name__ == "__main__":
    main()
