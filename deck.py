import random
from card import SUITS, RANKS, make_card

# Function to create a deck of cards
def build_deck():
    deck = []
    # Create a card for each suit and rank and add it to the list
    for suit in SUITS:
        for rank in RANKS:
            deck.append(make_card(suit, rank))
    # Return the list which is the deck of cards
    return deck

# Function to shuffle the deck
def shuffle_deck(deck):
    random.shuffle(deck)

# Function to deal cards from the deck
def deal(deck, count):
    # Check if the count is valid
    if count > len(deck):
        raise ValueError("Not enough cards to deal")
    # Deal the specified number of cards and remove them from the deck
    dealt = deck[:count]
    del deck[:count]
    return dealt