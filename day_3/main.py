print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("You're at a cross road. Where do you want to go?")
cross_road = input("Type \"left\" or \"right\"\n").lower()
if cross_road == "left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    lake_choice = input("Type \"wait\" to wait for a boat. Type \"swim\" to swim across.\n").lower()
    if lake_choice == "swim":
        print("You get attacked by an angry trout. Game Over.")
    elif lake_choice == "wait":
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        door_choice = input("One red, one yellow and one blue. Which colour do you choose?\n").lower()
        if door_choice == "red":
            print("It's a room full of fire. You die in a very arsonist way")
        elif door_choice == "yellow":
            print("Good intuition. It's the treasure chamber.")
        elif door_choice == "blue":
            print("Choosing your favourite colour didn't save you this time. You end up in a room full of beasts. You die in a very gore way.")
        else:
            print("Take a valid room next time. Your characters stays studying ortography until he dies of starvation and dehydration.")
    else:
        print("Make a valid decision next time. Your character dies because of indecision")
elif cross_road == "right":
    print("You fell into a hole. Game Over.")
else:
    print("Take a valid direction the next time. Your charachter ends up dead of indecision.")