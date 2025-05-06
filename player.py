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

# Function to check if the player has a specific suit in their hand
def has_suit(player, suit):
    for card in player['hand']:
        if card['suit'] == suit:
            return True
    return False

# Function to play a card from the player's hand
def play_card(player, lead_suit=None):
    # Show the player's hand and select valid cards to play
    hand = player['hand']
    valid = []
    if lead_suit and has_suit(player, lead_suit):
        for i in range(len(hand)):
            if hand[i]['suit'] == lead_suit:
                valid.append(i)
    else:
        valid = list(range(len(hand)))
    # Print the player's hand with valid cards marked
    for i in range(len(hand)):
        mark = '*' if i in valid else ' '
        print(f"{i+1}. {card_str(hand[i])} {mark}")
    # Prompt the player to select a card to play (within the constraints)
    while True:
        choice = input(f"{player['name']}, select a card to play (1-{len(hand)}): ")
        if not choice.isdigit():
            print("Invalid input, enter a number.")
            continue
        idx = int(choice) - 1
        if idx not in valid:
            print("You must follow suit if possible. Try again.")
            continue
        # Return the selected card and remove it from the hand
        return hand.pop(idx)