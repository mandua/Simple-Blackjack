import random

#1) Beginning info
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
dealer = []
player = []

#2) Print out instructions and welcome and if they want to play
print("\nWelcome to the game of Blackjack! In this game, you will be dealt with two cards to start. If you press to hit, then you will be dealt another card. If you choose to stay, then it will be the dealer's turn to play. Since this is only a simple version of Blackjack, we only use the cards 2 - 11, as well as the dealer has to hit until his hand is at least 17. Then, whoever has the better hand at the end wins!\n")

wantToPlay = input("Press enter to begin, or 'N' to stop: ")

#3) Conditionals and replay function
def playA(playAgain):
    #4) Reset variables for a new game
    cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    dealer = []
    player = []

    #5) Start a new game if the user wants to play again
    if playAgain == "":
        #6) Deal the player's starting hand
        for i in range(2):
            ranIndexNum = random.randint(0, len(cards) - 1)
            player.append(cards[ranIndexNum])
        print("Here is your hand: " + str(player))

        #7) Check if the player immediately wins or busts
        if sum(player) == 21:
            print("You win! :)")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return
        elif sum(player) > 21:
            print("You busted! :(")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return

        #8) Ask the player if they want to hit or stay
        option = input("Enter 'H' if you want to hit(get another card) or 'S' if you want to stay(let the dealer play): ")
        while option not in ["H", "S"]:
            option = input("Please enter H or S: ")

        #9) Continue dealing cards while the player keeps hitting
        if option == "H":
            while option == "H":
                ranIndexNum = random.randint(0, len(cards) - 1)
                player.append(cards[ranIndexNum])
                print("Here is your hand: " + str(player))

                #10) Check if the player wins or busts after hitting
                if sum(player) == 21:
                    print("You win! :)")
                    playA(input("\nPress enter to play again, or 'N' to stop: "))
                    return
                elif sum(player) > 21:
                    print("You busted! :(")
                    playA(input("\nPress enter to play again, or 'N' to stop: "))
                    return
                option = input("Enter 'H' if you want to hit(get another card) or 'S' if you want to stay(let the dealer play): ")
                while option not in ["H", "S"]:
                    option = input("Please enter H or S: ")
            print("Dealer's turn!\n")
        elif option == "S":
            print("Dealer's turn!\n")

        #11) Deal the dealer's starting hand
        for i in range(2):
            ranIndexNum = random.randint(0, len(cards) - 1)
            dealer.append(cards[ranIndexNum])
        print("Here is the dealer's hand: " + str(dealer))

        #12) Dealer must hit until reaching at least 17
        while not(sum(dealer) >= 17):
            ranIndexNum = random.randint(0, len(cards) - 1)
            dealer.append(cards[ranIndexNum])
            print("Here is the dealer's hand: " + str(dealer))
        print("The dealer has finalized his hand.")

        #13) Determine who wins the game
        if sum(dealer) > 21:
            print("The dealer has busted. You win! :)")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return
        elif sum(player) > sum(dealer):
            print("You have a better hand. You win! :)")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return
        elif sum(dealer) > sum(player):
            print("The dealer has a better hand. You lose! :(")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return
        else:
            print("It's a tie!")
            playA(input("\nPress enter to play again, or 'N' to stop: "))
            return

    #14) End the program if the user chooses not to play again
    else:
        print("Have a good day!")
        exit()


#15) Begin the first game if the user wants to play
if wantToPlay == "":
    #16) Deal the player's starting hand
    for i in range(2):
        ranIndexNum = random.randint(0, len(cards) - 1)
        player.append(cards[ranIndexNum])
    print("Here is your hand: " + str(player))

    #17) Check if the player immediately wins or busts
    if sum(player) == 21:
        print("You win! :)")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()
    elif sum(player) > 21:
        print("You busted! :(")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()

    #18) Ask the player if they want to hit or stay
    option = input("Enter 'H' if you want to hit(get another card) or 'S' if you want to stay(let the dealer play): ")

    while option not in ["H", "S"]:
        option = input("Please enter H or S: ")

    #19) Continue dealing cards while the player keeps hitting
    if option == "H":
        while option == "H":
            ranIndexNum = random.randint(0, len(cards) - 1)
            player.append(cards[ranIndexNum])
            print("Here is your hand: " + str(player))

            #20) Check if the player wins or busts after hitting
            if sum(player) == 21:
                print("You win! :)")
                playA(input("\nPress enter to play again, or 'N' to stop: "))
                exit()
            elif sum(player) > 21:
                print("You busted! :(")
                playA(input("\nPress enter to play again, or 'N' to stop: "))
                exit()
            option = input("Enter 'H' if you want to hit(get another card) or 'S' if you want to stay(let the dealer play): ")
            while option not in ["H", "S"]:
                option = input("Please enter H or S: ")

        print("Dealer's turn!\n")

    elif option == "S":
        print("Dealer's turn!\n")

    #21) Deal the dealer's starting hand
    for i in range(2):
        ranIndexNum = random.randint(0, len(cards) - 1)
        dealer.append(cards[ranIndexNum])
    print("Here is the dealer's hand: " + str(dealer))

    #22) Dealer keeps hitting until reaching at least 17
    while not(sum(dealer) >= 17):
        ranIndexNum = random.randint(0, len(cards) - 1)
        dealer.append(cards[ranIndexNum])
        print("The dealer has decided to hit.")
        print("Here is the dealer's hand: " + str(dealer))
    print("The dealer has finalized his hand.")

    if sum(dealer) > 17 and sum(dealer) <= 21:
        print("The dealer has decided to stay.")

    #23) Determine who wins the game
    if sum(dealer) > 21:
        print("The dealer has busted. You win! :)")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()
    elif sum(player) > sum(dealer):
        print("You have a better hand. You win! :)")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()
    elif sum(dealer) > sum(player):
        print("The dealer has a better hand. You lose! :(")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()
    else:
        print("It's a tie!")
        playA(input("\nPress enter to play again, or 'N' to stop: "))
        exit()

#24) End the program if the user does not want to play
else:
    print("Well then, have a good day!")
    exit()