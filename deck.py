import random
from card import SUITS, RANKS, make_card

# Function to create a deck of cards
def build_deck():
    '''create a deck of cards'''
    deck = []
    # Create a card for each suit and rank and add it to the list
    for suit in SUITS:
        for rank in RANKS:
            deck.append(make_card(suit, rank))
    # Return the list which is the deck of cards
    return deck

# Function to shuffle the deck
def shuffle_deck(deck):
    '''shuffle the deck of cards'''
    random.shuffle(deck)

# Function to deal cards from the deck
def deal(deck, count):
    '''deal a specified number of cards from the deck'''
    # Check if the count is valid
    if count > len(deck):
        raise ValueError("Not enough cards to deal")
    # Deal the specified number of cards and remove them from the deck
    dealt = deck[:count]
    del deck[:count]
    return dealt

# Function to draw the top card from the deck
def draw(deck):
    '''draw the top card from the deck'''
    if not deck:
        return None
    return deck.pop(0)

## tests

# build_deck() should return a deck which is a list of 52 cards

# shuffle_deck(deck) should shuffle the deck in place

# deal(deck, 5) should return a list of 5 cards and remove them from the deck

# draw(deck) should return the top card from the deck and remove it from the deck