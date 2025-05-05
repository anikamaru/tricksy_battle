# Lists to store all the suits and ranks
SUITS = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q']  # Kings removed

# Function to create cards
def make_card(suit, rank):
    # Check if suit and rank are valid
    if suit not in SUITS:
        raise ValueError(f"Invalid suit: {suit}")
    if rank not in RANKS:
        raise ValueError(f"Invalid rank: {rank}")
    # Return dictionary storing suit and rank (value is index, i.e., power of the rank)
    return {'suit': suit, 'rank': rank, 'value': RANKS.index(rank)}

# Return the string representation of a card
def card_str(card):
    return f"{card['rank']} of {card['suit']}"