from card import card_str

# Function to create a player (dictionary with name, hand, and score)
def make_player(name):
    return {'name': name, 'hand': [], 'score': 0}

# Function to receive cards and add them to the player's hand
def receive_cards(player, cards):
    player['hand'].extend(cards)

# Function to print the player's hand
def show_hand(player):
    print(f"{player['name']}'s hand:")
    for i in range(len(player['hand'])):
        print(f"  {i+1}: {card_str(player['hand'][i])}")