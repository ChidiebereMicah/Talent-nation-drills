"""
C1. Balanced Brackets (Revision: Use a Stack)

Suggested time: 25 to 30 minutes

Problem
Write is_balanced(text) -> bool that returns True if every opening bracket (, [ or { has a matching closing bracket in the correct order. Ignore every other character.
Examples
is_balanced("(a + b) * [c - d]")   # True
is_balanced("{[()]}")              # True
is_balanced("([)]")                # False
is_balanced("((")                  # False
is_balanced("}{")                  # False
is_balanced("")                    # True

Constraints
Use a list as a stack (append to push, pop to remove). No recursion.
Use a dictionary that maps each closing bracket to its opening bracket.
Pure function: no printing inside.
Do not import libraries.
Test at least these cases: a closing bracket when the stack is empty, openers left over at the end, and mixed bracket types.
Bonus
Write max_depth(text) that returns the deepest nesting level of a balanced string: max_depth("((a)(b))") gives 2 and max_depth("") gives 0. No max().
What this gauges: Can you recognize when the last thing in must be the first thing out? Can you choose a data structure for the job?
"""
def is_balanced(text):
    brackets = {'(':')',
                '[':']',
                '{':'}'
               }
    stack = []

    for bracket in text:
        if bracket in brackets:
            stack.append(brackets[bracket])
        elif bracket in brackets.values():
            if not stack:
                return False
            if bracket == stack[-1]:
                stack.pop()
            else:
                return False

    return not stack
        
print(is_balanced("(a + b) * [c - d]"))  # True
print(is_balanced("{[()]}"))              # True
print(is_balanced("([)]"))                # False
print(is_balanced("(("))                  # False
print(is_balanced("}{"))                  # False
print(is_balanced(""))                    # True

            