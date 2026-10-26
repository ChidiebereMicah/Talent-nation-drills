"""
Fibonacci Sequence — Even Sum
Suggested time: 15–20 minutes
Problem
Print the first N numbers of the Fibonacci sequence. Calculate the sum of only the even numbers in that sequence. Finally, print the sequence in reverse order.
Examples
Input: N = 8
Sequence: 0, 1, 1, 2, 3, 5, 8, 13
Even Sum: 10 (which is 0 + 2 + 8)
Reversed: 13, 8, 5, 3, 2, 1, 1, 0
Constraints
Generate the sequence using a loop (no recursion).
Do not store the sequence in an array/list to reverse it. Print the reversed sequence using mathematical logic or string-building without [::-1] or .reverse().
Do not use sum().
Do not import libraries.
What This Tests: Variables, state swapping, loops, conditionals, and string/number manipulation.

"""

def fibonacci_sequence(term):
    term0, term1 = 0, 1
    even_sum = 0
    evens = '0'
    sequence = "0, 1"
    for i in range(term - 2):
        next_term = term0 + term1
        term0, term1 = term1, next_term
        if i > 0 and next_term % 2 == 0:
            evens += ' + ' + str(next_term)
            even_sum += next_term
        sequence += ", " + str(next_term)

    sequence_list = sequence.split(", ")
    reverse = ""
    for i in range(len(sequence_list)-1, -1, -1):
        if i == 0:
            reverse += sequence_list[i]
        else:
            reverse += sequence_list[i] + ", "
    return(f"Sequence: {sequence}\n"
           f"Even Sum: {even_sum} (which is {evens})\n"
           f"Reversed: {reverse}"
        )


print(fibonacci_sequence(8))