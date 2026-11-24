print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
# If we asks for numbers, casting to integer is needed. Input always return strings
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# we need the tip as a percentage
percentage = 1 + tip / 100
operation = (bill / people) * percentage

# using :.2f in the print allows to control the number of decimals. Usually 2
print(f"Each person pays {operation:.2f}")