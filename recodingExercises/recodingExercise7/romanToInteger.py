"""
7. Roman to Integer
Suggested time: 20–25 minutes
Problem
Given a string representing a Roman numeral, convert it to an integer. Symbols: I = 1, V = 5, X = 10, L = 50, C = 100, D = 500, M = 1000. If a smaller numeral appears before a larger one, subtract it (e.g., IV = 4, IX = 9); otherwise, add it.
Examples
Input: "III" → 3
Input: "LVIII" → 58 (L = 50, V = 5, III = 3)
Input: "MCMXCIV" → 1994 (M = 1000, CM = 900, XC = 90, IV = 4)
Constraints
Store Roman numeral mappings in a dictionary.
Use a while loop to traverse the string.
Do not import libraries.
Do not hardcode the answers.
What This Tests: Dictionaries, string indexing, look-ahead logic, and conditionals.
"""
def romanToInt(s: str) -> int:
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    arabic = 0

    i = 0
    while i < len(s):
        if s[i] not in roman:
            return "Invalid input"
        if i != len(s)-1 and roman[s[i]] < roman[s[i+1]]:
            arabic -= roman[s[i]]
        else:
            arabic += roman[s[i]]
        i += 1

    return arabic

s = "III"
q = "MCMXCIV"
print(romanToInt(s))
print(romanToInt(q))