from deck import build_deck, shuffle_deck, deal
from player import make_player, receive_cards

# Function to start the game
def start_game():
    # Create and shuffle the deck
    deck = build_deck()
    shuffle_deck(deck)
    # Create players and deal their cards
    players = [make_player("Player 1"), make_player("Player 2")]
    for p in players:
        receive_cards(p, deal(deck, 8))

# Start the game
start_game()