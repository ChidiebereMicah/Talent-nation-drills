"""
C2. Reverse a Stack In-Place: Recursive Auxiliary Functions
Suggested time: 25 to 30 minutes
Concept: Auxiliary recursive functions (recursion inside recursion) and in-place data structure manipulation.
Problem
Write a recursive function reverse_stack(stack) that reverses a list in-place so that the top element becomes the bottom element and the bottom element becomes the top element. Reverse the original list directly without creating another data structure.
Example
Input:   stack = [1, 2, 3, 4, 5]
          reverse_stack(stack)
          print(stack)
Output:  [5, 4, 3, 2, 1]

Hints
Think about how to remove the top element recursively.
Consider writing an auxiliary recursive function that inserts an element at the bottom of the stack.
First remove all elements recursively, then insert them back at the bottom in the correct order.
Constraints
Zero for or while loops.
Do not create any new lists, tuples, or sets.
You may only use .append() and .pop() to modify the original list.
Use auxiliary recursive functions where necessary.
Reverse the original list in-place.
Do not use slicing or built-in reversing methods.
Do not import libraries.
What this tests: Recursion inside recursion, auxiliary functions, stack operations, in-place manipulation, call-stack management, and backtracking.

"""

def reverse_stack(stack):
    first = stack[0]
    if stack[-1] == 1:
        return stack
    return stack.pop()