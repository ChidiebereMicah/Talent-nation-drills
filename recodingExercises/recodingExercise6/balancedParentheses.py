"""
Balanced Parentheses — With Multiple Bracket Types
Suggested time: 15–20 minutes
Problem
Determine whether a string contains balanced brackets. Every opening bracket must have a matching closing bracket of the same type in the correct order. Handle round (), square [], and curly {} brackets.
Examples
Input: "(a + b) * [c - d]" → Balanced
Input: "(a + b)]" → Not balanced (mismatched type)
Input: "((a + b)" → Not balanced (unclosed)
Input: "[(a + b) * {c - d}]" → Balanced
Input: "([)]" → Not balanced (wrong order)
Constraints
Use a loop and a list as a stack (append to push, pop to check).
Do not import libraries.
Do not use a simple counter — a counter alone cannot detect mismatched types.
Ignore all characters that are not brackets.
At the end, the stack must be empty.
Do not hardcode the answer.
What This Tests: Strings, loops, lists as stacks, conditionals, matching pairs, and algorithmic reasoning

"""

def balanced_parens(text):
    enclosures = {'(': ')',
                  '[': ']',
                  '{': '}'}
    unbalanced = []

    for ch in text:
        if ch not in enclosures.items():
            continue
        if ch in enclosures:
            unbalanced.append(enclosures[ch])
        elif ch in unbalanced:
            unbalanced.pop
        elif ch in enclosures.values():
            return "Not balanced"

    if not unbalanced:
        return "Balanced"
    return "Not balanced"

print(balanced_parens( "((a + b)"))
print(balanced_parens("[(a + b) * {c - d}]"))