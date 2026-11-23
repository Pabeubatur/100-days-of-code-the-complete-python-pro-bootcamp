# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

import art

print(art.logo)

bid_participants = {}
more_users = True

# we loop from the beginning, so we don't repeat the variables on the next loop
while more_users:

    user_name = input("What is your name?\n").lower()
    bid_price = int(input("what is your bid?\n").lower())

    bid_participants[user_name] = bid_price

    question_users = input("There are other users who want to bid?\n").lower()
    if question_users == "no":
        more_users = False
    elif question_users == "yes":
        # if the user wants to add new bidders, we should clean the screan
        # this can also be achieved with import os and os.system("clear")
        print("\n" * 100)

# find the winnner
# in this case we used the native function max to get the key with the maximum value
# but it is recommended to make your own function if you're learning, as you know how this code works
# but you don't know it's design.
max_bid = max(bid_participants, key=bid_participants.get)
bid_winner = bid_participants[max_bid]
print(f"The winner is {max_bid} with a bid of {bid_winner}")