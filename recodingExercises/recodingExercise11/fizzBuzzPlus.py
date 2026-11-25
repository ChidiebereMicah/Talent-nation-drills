"""
1. FizzBuzz Plus

Suggested time: 15–20 minutes

Problem
Write fizzbuzz_plus(n) that returns a list of strings for the numbers 1 to n:
Multiples of 3 include "Fizz", multiples of 5 include "Buzz", multiples of 7 include "Bazz".
If a number is a multiple of more than one, join the words in that order.
If it is a multiple of none, use the number as a string.
Examples
3   → "Fizz"
15  → "FizzBuzz"
21  → "FizzBazz"
35  → "BuzzBazz"
105 → "FizzBuzzBazz"
4   → "4"
fizzbuzz_plus(0) → []
Constraints
Build each result by adding words to a string one rule at a time. Do not write a separate if branch for every combination.
Return the list. Print from outside the function.
What this gauges: Loops, modulo, and building a string step by step.

"""
def fizzbuzz_plus(num):
    output = []
    if num <= 0:
        return []
    if num % 3 == 0:
        output.append("Fizz")
    if num % 5 == 0:
        output.append("Buzz")
    if num % 7 == 0:
        output.append("Bazz")
    if not output:
        return str(num)
    return output

num1 = 105
num2 = 15
num3 = 21
num4 = 35
num5 = 3
num6 = 4
print("".join(fizzbuzz_plus(num6)))
    