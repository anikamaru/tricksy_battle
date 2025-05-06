# TRICKSY BATTLE
A console-based Python implementation of the Tricksy Battle card game using a 48-card deck without Kings

## PROJECT STRUCTURE
- **card.py**: File containing code related to a card
- **deck.py**: File containing code related to a deck of cards
- **player.py**: File containing code related to a player
- **game.py**: File containing code related to the state of the game

## INSTALLATION & USAGE
Clone the repository and then run the game by typing:
`git clone https://github.com/anikamaru/tricksy_battle.git tricksy_battle`
`python game.py`

## HOW PLAYERS PLAY
On each turn the current player’s hand is displayed with each card on a separate line prefixed by a number starting at 1. Cards that can legally be played (following suit if possible) are marked with an asterisk (*). The player types the number corresponding to the desired card to play and presses Enter.

## GAMEPLAY RULES
Each player is dealt eight cards and a random leader starts the first trick. The leader may play any card; the opponent must follow suit if able. The highest card of the lead suit wins the trick and the winner scores one point. After each trick the top card of the deck is revealed (no scoring effect). When both players have four cards in hand and at least eight cards remain in the deck, four new cards are dealt to each. The game ends when a player reaches a 9–1 score or when all cards have been played. If the final score is 16–0, the player with zero points has shot the moon and their score becomes 17 points.

## LIMITATIONS
- No AI opponent by default
- Terminal-based only (no graphical interface)
- Once a game ends, its data is lost (no persistence or replay)