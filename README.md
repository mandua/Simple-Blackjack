# Blackjack
A simple command-line Blackjack game written in Python. Play against the dealer, choosing to hit or stay, with the goal of getting closer to 21 than the dealer without going over.

## How to Play
You'll be greeted with the rules, then prompted to begin:
Press enter to begin, or 'N' to stop:

Press Enter to start a hand, or type 'N' to exit immediately.

### Gameplay
1. You're dealt two cards, and your hand total is shown.
2. If your hand totals exactly 21, you win instantly. If it's over 21, you bust and lose instantly.
3. Otherwise, you're asked to **hit** (`H`) to draw another card, or **stay** (`S`) to end your turn.
   - You can keep hitting as many times as you like, as long as you haven't busted.
4. Once you stay (or after your final hit doesn't bust or hit 21), the dealer plays automatically, drawing cards until their hand totals 17 or more.
5. The winner is determined:
   - If the dealer busts (over 21), you win.
   - If your total is higher than the dealer's, you win.
   - If the dealer's total is higher, you lose.
   - If totals are equal, it's a tie.
6. After each hand, you're asked whether you want to play again (press Enter) or stop (`N`).

## Rules & Card Values
- This is a simplified version of Blackjack: cards are valued **2 through 11** only (no face cards, no suits, and no distinct Ace-as-1-or-11 logic — 11 is just dealt as a fixed value).
- Each card is drawn independently and at random, with replacement (the same value can be drawn multiple times, similar to drawing from an infinite deck).
- The dealer must keep hitting until their hand totals at least 17, matching standard Blackjack dealer rules.

## Notes
- This is a simplified, learning-oriented implementation. Differences from standard Blackjack include the absence of face cards/suits, no betting, and no special Ace handling.
- The game loops via recursive calls (`playA`) each time the player chooses to play again, rather than using an iterative loop.
