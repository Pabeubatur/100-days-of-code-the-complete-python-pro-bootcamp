print("Welcome to the Band Name Generator Project")

# It's important to add a breakline at the end so we input the value in a different line. Cleaner and more efficient
city = input("In which city did you grow up?\n")
pet = input("Which is the name of your pet?º\n")

# We can use a f-string to acomplist this in a cleaner way. But concatenation is also valid and it's important to know
# which data type can be concatenated and in which conditions.
# usually you can concatenate the same type of data. string and int cannot be concatenated together.
print("The name of your band is" + " " + city + " " + pet + "!")