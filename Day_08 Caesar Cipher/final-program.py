# TODO-1: Import and print the logo from art.py when the program starts.
import art

print(art.logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# TODO-2: What happens if the user enters a number/symbol/space?
# TODO-3: Can you figure out a way to restart the cipher program?

def caesar(original_text, shift_amount, encode_or_decode):
    output_text = ""

    # this should be outside, otherwise it woudl flip negatives to positives and viceversa
    if encode_or_decode == "decode":
        shift_amount *= -1

    for letter in original_text:
        # as there are are many ways to check if a value exist in a list, this is the more legible
        # we can use not statement at if statement staart or before 'in' statement
        if letter not in alphabet:
            output_text += letter
            continue

        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        output_text += alphabet[shifted_position]
    print(f"Here is the {encode_or_decode}d result: {output_text}")

    # a 'return' statement is not needed if a function executes an action and not an operation

# I use a boolean and assigns it True to enter the loop
want_to_continue =  True

while want_to_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # this line works as hardcoded values so I don't have to input manual values each time I want to debug or test the code
    # caesar("3", 5, "encode")
    caesar(original_text=text, shift_amount=shift, encode_or_decode=direction)
    # once we call the function the first time, we give the user a choice. If It doesn't want to continue, I change the boolean value to False
    # in order to exit the loop and finish the program
    user_choice = input("Type 'yes' if you want to go again. Otherwise, type 'no'.").lower()
    if user_choice == "no":
        want_to_continue = False
        # THis is a wholesome program, so we say goodbye when the user exits
        print("Goodbye ;)")
