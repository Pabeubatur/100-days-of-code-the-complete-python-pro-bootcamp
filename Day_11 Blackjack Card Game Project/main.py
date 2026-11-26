import random
import art

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def final_result(user_list, computer_list, user_sum, computer_sum):
    """Print your final hand, computer's final hand, your final score and computer final score for every ending of the game."""
    print(f"    Your final hand: {user_list}, final score: {user_sum}")
    print(f"    Computer final hand: {computer_list}, final score: {computer_sum}")

def blackjack():
    start_game = input("Do you want to play a game of Blackjack? Type 'y' or 'n':   ").lower()
    # Clean the screen
    print("\n" * 20)
    if start_game == "y":
        # Print the logo if the game is started
        print(art.logo)
        # DEAL TWO CARDS TO USER AND COMPUTER
        # we can't store the random draw in a variable in order to minimize code because it will store the same result
            # random_draw = random.choice(cards)
            # user_hand = [random.choice(cards), random.choice(cards)]
            # computer_hand = [random.choice(cards),random.choice(cards)]
            # Output:
            # user_hand = [6, 6]
            # computed_hand = [6, 6]
        user_hand = [random.choice(cards), random.choice(cards)]
        computer_hand = [random.choice(cards), random.choice(cards)]
        # always have hardcoded values to make test for every stage of the code
        # computer_hand = [2, 2]
        # user_hand = [11, 10, 2]
        draw_cards =  True

        # ADD THE USER AND COMPUTER SCORES
        while draw_cards:
            user_score = sum(user_hand)
            computer_score = sum(computer_hand)

            # BLACKJACK (SCORE 21) CHECK
            # for the initial blackjack we don't need to tally a score,
            # this is for the second loop in case the user wants to draw a second card
            if user_score == 21 or computer_score == 21:
                if computer_score == 21:
                    # this variable is very convenient because we use this print in every game ending
                    final_result(user_hand, computer_hand, user_score, computer_score)
                    print("Computer had a Blackjack! You loose")
                    blackjack()
                    # for these endings except the three final ones, we need an additional return
                    # if we don't write a return, when we press 'n' after the call, the program will continue to line 64
                    return
                elif user_score == 21:
                    final_result(user_hand, computer_hand, user_score, computer_score)
                    print("You have a Blackjack!. You win")
                    blackjack()
                    return

            # for the first draw it won't take effect, as It's impossible to surpass with two cards, even if we draw
            # two aces, because the ACE CHECK will prevent we reach 22.
            # BUST CHECK
            if user_score > 21:
                # does he have an ace?
                # ACE CHECK
                if 11 in user_hand:
                    # index() method returns ValueError, so we can't store it in a variable because
                    # if we don't a get an 11, it will raise an error and stop the program
                    user_hand[user_hand.index(11)] = 1
                    if sum(user_hand) > 21:
                        final_result(user_hand, computer_hand, user_score, computer_score)
                        print("You Busted. You loose")
                        blackjack()
                        return
                    # if we swap the ace value from 1 to 11, it is necessary to recalculate user_score
                    # if not, we will get the previous score including the ace with a value of 11
                    user_score = sum(user_hand)
                else:
                    final_result(user_hand, computer_hand, user_score, computer_score)
                    print("You Busted. You loose")
                    blackjack()
                    return

            # In order to debug, we need to know computer's hand and score
            # In a production code we should hide it and only show user hand and score, and computer's first card
            # print(f"Your cards: {user_hand}, computers cards: {computer_hand}")
            print(f"Your cards: {user_hand}, your actual score: {user_score}")
            # print(f"Your actual score is {user_score}")
            # print(f"The computer score is {computer_score}")
            print(f"Computer's first card: {computer_hand[0]}")

            # DRAW NEW CARD
            draw_card = input("Do you want to draw another card? Press 'y' or 'n':   ").lower()
            if draw_card == 'y':
                user_hand.append(random.choice(cards))
            else:
                # COMPUTER DRAW
                draw_cards = False
            # In this stage, we tabbed the code inside a while loop, starting from the score calculator, in order to
            # make the code not repetitive

        #once we exit the loop, the computer draws
        computer_draw = True
        while computer_draw:
            if computer_score < 17:
                computer_hand.append(random.choice(cards))
                # recalculate the computer score
                computer_score= sum(computer_hand)
            else:
                computer_draw = False

        # COMPUTER BUST
        if computer_score > 21:
            final_result(user_hand, computer_hand, user_score, computer_score)
            print(f"Computer Busted. You win with a final score of {user_score}")
            blackjack()
            return

        # FINAL SCORE
        final_result(user_hand, computer_hand, user_score, computer_score)

        if user_score == computer_score:
            print("It's a draw!")
            # at this stage, we moved all the existing code into a function, so we could exit the loop
            # and start a fresh new game
            blackjack()
        elif user_score > computer_score:
            print("You win")
            # In this case, It's not necessary a return, because after input "n" when we call the function, the
            # program returns to this line, but the function ends here and stops
            blackjack()
        else:
            print("You loose")
            blackjack()

    else:
        return

blackjack()