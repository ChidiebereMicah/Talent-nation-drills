"""
6. Leap Year Checker

Suggested time: 12–15 minutes
Problem
Write a program that determines whether a given year is a leap year. A year is a leap year if it is divisible by 4, and it is not divisible by 100 unless it is also divisible by 400.
Examples
Input: 2024 → 2024 is a leap year
Input: 1900 → 1900 is not a leap year
Input: 2000 → 2000 is a leap year
Input: 2023 → 2023 is not a leap year
Constraints
Use input() and convert the year to an integer.
Use if / elif / else and the % operator.
Do not use any libraries.
Do not hardcode the answer.
Handle the divisible-by-100-but-not-400 case correctly.
What This Tests: Conditionals, modulo, edge-case logic, and input handling.
Optional Stretch: Print the next 3 leap years after the input year using a loop.
"""

def leap_year_checker(year):
    if year < 1:
        return "Please enter a positive year."
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
        return True

    return False

check = input("Do you want to check a leap year?\nPress Y to check, any key to exit: ")
check_count = 1
while check.lower() == 'y':
    print(f'===== Check {check_count} =====')
    try:
        year = int(input("Please enter year to check leapyearness: "))
        leap_years_after = int(input('Enter the number of leap years following: '))
        if year < 1 or leap_years_after < 0:
            raise ValueError
    except ValueError:
        print("You have not entered a valid year or number of leap years.")
        continue

    if leap_year_checker(year):
        print(f"{year} is a leap year.")
    else: 
        print(f"{year} is not a leap year.")

    found = 0
    candidate = year + 1

    if leap_years_after > 0:
        print("The leap years following are: ", end="")
        while found < leap_years_after:
            if leap_year_checker(candidate):
                print(candidate, end=" ")
                found += 1

            candidate += 1

    check_count += 1
    check = input("\nDo you want to check a leap year?\nPress Y to check, any key to exit: ")

print('\nThanks for using this service.')