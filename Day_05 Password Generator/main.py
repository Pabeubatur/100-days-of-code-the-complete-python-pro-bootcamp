import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# the method list() also works
def string_to_list(string):
    final_list = []
    for character in string:
        final_list.append(character)

    return final_list

def randomise_pattern(user_list):
    random.shuffle(user_list)
    # shuffle() method is an action function, so it doesn't return anything, we need to redirect the output into a variable
    # either list or string. In this case we redirect the output to a string using .join() method
    result = ''.join(user_list)
    return result

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pwd_letters = ""
for number in range(1,nr_letters +1):
    # len() gives the total amount  of elements, but lists starts from zero
    # we need to substract one so we don't get a IndexError
    random_number = random.randint(0,len(letters) - 1)
    # we had two choices: use a randint() to get a random element in a list, or use random.choice()
    pwd_letters += letters[random_number]

pwd_symbols = ""
for symbol in range(1, nr_symbols + 1):
    random_number = random.randint(0, len(symbols) - 1)
    pwd_symbols += symbols[random_number]

pwd_numbers = ""
for number in range(1, nr_numbers + 1):
    random_number = random.randint(0, len(numbers) - 1)
    pwd_numbers += numbers[random_number]

not_patterned_string = pwd_letters + pwd_symbols + pwd_numbers

# print(not_patterned_string)
# for the hard version we need to randomise the order
# I'm going to use random.shuffle(), but first I need to convert the string to a list

pattern_listed = string_to_list(not_patterned_string)
# print(pattern_listed)

randomised_list = randomise_pattern(pattern_listed)
print(randomised_list)