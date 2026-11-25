def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            return False
        return True

    else:
        return False

user_year = int(input("Insert your desired year and I'll tell you if It is leap year or not: "))
print(is_leap_year(user_year))