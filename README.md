# Simple Blackjack Game

## Overview

This project is a simple text-based Blackjack game written in Python. The player competes against a computer dealer by trying to get a hand value as close to 21 as possible without going over.

The game uses a simplified deck consisting of card values 2 through 11, where 11 represents an Ace. The dealer follows standard Blackjack rules by continuing to draw cards until their hand value reaches at least 17.

## Features

* Deal two starting cards to the player
* Hit or stay options
* Dealer AI that automatically plays its turn
* Bust detection for both player and dealer
* Win, lose, and tie outcomes
* Replay functionality
* Input validation for user choices

## How to Play

1. Run the program.
2. Press Enter to start a game or type `N` to quit.
3. You will receive two cards.
4. Choose:

   * `H` to hit and receive another card
   * `S` to stay and end your turn
5. The dealer will play automatically after you stay.
6. The winner is determined by comparing hand totals:

   * Closest to 21 wins
   * Going over 21 results in a bust
   * Equal totals result in a tie

## Rules

* Cards range from 2 to 11.
* 11 represents an Ace.
* The dealer must continue drawing cards until their total is at least 17.
* If the player's total exceeds 21, the player busts.
* If the dealer's total exceeds 21, the dealer busts.
* The higher total wins if neither player busts.

## Requirements

* Python 3.x

## Running the Program

Open a terminal in the project folder and run:

```bash
python main.py
```

## Project Structure

```text
blackjack/
│
├── main.py
└── README.md
```

## Future Improvements

* Add face cards (Jack, Queen, King)
* Add proper Ace handling (1 or 11)
* Use a full 52-card deck
* Track wins and losses
* Display only one dealer card until the player's turn ends
* Replace replay recursion with a game loop

## Author

Created as a Python Blackjack project for learning programming concepts such as functions, loops, conditionals, lists, user input, and random number generation.
