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

# Function to return the string representation of a card
def card_str(card):
    return f"{card['rank']} of {card['suit']}"

# Function to compare two cards
def card_compare(card1, card2):
    # Compare by rank index
    v1 = RANKS.index(card1['rank'])
    v2 = RANKS.index(card2['rank'])
    # Positive if card1 > card2, negative if card1 < card2, zero if equal
    if v1 != v2:
        return v1 - v2
    # If equal rank, let suit order be the tiebreaker
    return SUITS.index(card1['suit']) - SUITS.index(card2['suit'])