import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# the gist is: you win agains the lower and loose agains the upper.
# paper (1) wins against rock (0), but loses agains scissors (2)
# we have a problem with rock (0) and scissors (2).
# rocks is defeated by paper (1), but scissors (2) are defeated by rocks. This is an exception we should address
# scissors defeats papers 2 > paper (1). But It is defeater by rocks, althougs rocks (0) is lower than scissors (2). Second exception
choices_list = [rock, paper, scissors]
computer_choice = random.randint(0,2)
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors\n"))
# user_choice = 3

# we lacked a validation the first time. If we use a list It is advisable to always validate the user input so we don't get an Index Error Out of range
if user_choice >= 0 and user_choice <= 2:
    print(f"User chose {choices_list[user_choice]}")

if user_choice < 0 or user_choice > 2:
    print("Please input a valid number. You lose")

elif user_choice == computer_choice:
    print(f"Computer chose ´{choices_list[computer_choice]}")
    print("It's a draw")
    # if I get scissors, although 2 is greater than 0, scissors lose agains rocks
elif user_choice == 2 and computer_choice == 0:
    print(f"Computer chose ´{choices_list[computer_choice]}")
    print("You lose")
    # If i get rock agains scissors, although 2 is greater than 0, rock win agains scissors
elif user_choice == 0 and computer_choice == 2:
    print(f"Computer chose ´{choices_list[computer_choice]}")
    print("You win")
    # this is true for paper and scissors, but not for scissors although scissors is greather than rock, scissors are beaten by rocks
elif user_choice >= computer_choice:
    print(f"Computer chose ´{choices_list[computer_choice]}")
    print("You win")
    # this is true for paper and scissors, but not fork rocks. If I get rocks and computer gets scissors, I should win.
elif user_choice <= computer_choice:
    print(f"Computer chose ´{choices_list[computer_choice]}")
    print("You lose")
