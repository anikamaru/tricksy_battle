import random
from deck import build_deck, shuffle_deck, deal, draw
from player import make_player, receive_cards, show_hand, play_card
from card import card_str, card_compare

# Function to start the game
def start_game():
    # Create and shuffle the deck   
    deck = build_deck()
    shuffle_deck(deck)
    # Create players and deal their cards
    players = [make_player("Player 1"), make_player("Player 2")]
    for p in players:
        receive_cards(p, deal(deck, 8))
    # Randomly select a leader
    leader = players[random.randint(0, 1)]
    # Return a tuple of deck, players, and leader
    return deck, players, leader

# Function for player to play a trick
def play_trick(deck, players, leader):
    # Start new round and select the leader to play first
    print(f"\n{leader['name']} leads this round.")
    lead = play_card(leader)
    lead_suit = lead['suit']
    print(f"{leader['name']} played {card_str(lead)}.")
    # Select the other player to play their card
    if leader is players[1]:
        other = players[0]
    else:
        other = players[1]
    reply = play_card(other, lead_suit)
    print(f"{other['name']} played {card_str(reply)}.")
    # Determine the winner of the round
    if reply['suit'] == lead_suit and card_compare(reply, lead) > 0:
        winner = other
    else:
        winner = leader
    # Update the winner's score and print the round's result
    winner['score'] += 1
    print(f"{winner['name']} wins the trick and now has {winner['score']} point(s).")
    # Draw the top card from the deck and show it
    shown = draw(deck)
    if shown:
        print(f"Revealed from deck: {card_str(shown)} (no effect on scoring)")
    else:
        print("Deck is empty, no card to reveal.")
    # Return the winner of the round
    return winner

# Function to deal 4 new cards if each player has 4 cards in hand
def deal_next(deck, players):
    # Check if all players have 4 cards in hand
    all_have_four = True
    for p in players:
        if len(p['hand']) != 4:
            all_have_four = False
            break
    # If all players have 4 cards and enough cards in deck, deal 4 new cards
    if all_have_four and len(deck) >= 8:
        for p in players:
            receive_cards(p, deal(deck, 4))
        print("Dealt 4 new cards to each player.")

# Function to check if the game has ended
def check_end(deck, players):
    # Get the scores of each player
    scores = []
    for p in players:
        scores.append(p['score'])
    # Check if one player has 9 points and the other has at least 1 point
    if 9 in scores and min(scores) >= 1:
        return True
    # Check if all players have no cards in hand
    for p in players:
        if len(p['hand']) != 0:
            return False
    return True

# Function to print the final results
def final_results(players):
    # Print the final scores of each player
    p1, p2 = players
    print(f"\nFinal scores -- {p1['name']}: {p1['score']}, {p2['name']}: {p2['score']}")
    # Check if player 1 shot the moon
    if (p1['score'] == 16 and p2['score'] == 0):
        p1['score'] = 17
        print(f"{p1['name']} shot the moon and wins with 17 points!")
    # Check if player 2 shot the moon
    elif (p2['score'] == 16 and p1['score'] == 0):
        p2['score'] = 17
        print(f"{p2['name']} shot the moon and wins with 17 points!")
    # Check if player 1 won
    elif (p1['score'] > p2['score']):
        print(f"{p1['name']} wins the game!")
    # Check if player 2 won
    elif (p1['score'] < p2['score']):
        print(f"{p2['name']} wins the game!")
    # Check if it's a tie
    else:
        print("It's a tie!")

# Function to run the game
def run_game():
    # Start the game and get the initial state
    deck, players, leader = start_game()
    # Count each round till the game ends
    count = 0
    while not check_end(deck, players):
        count += 1
        # Print the rounds and players' hands
        print(f"\n-- Round {count} --")
        for p in players:
            show_hand(p)
        # Play a trick and determine the winner
        leader = play_trick(deck, players, leader)
        # If 4 cards each, deal 4 new cards
        deal_next(deck, players)
    # Print the final scores and results after the game ends
    final_results(players)

# Call the run game function to start the game
if __name__ == '__main__':
    run_game()