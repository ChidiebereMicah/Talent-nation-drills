"""
3. Vowels and Consonants
Suggested time: 15–20 minutes
Problem
Write count_letters(text) that returns (vowels, consonants). Count only letters. Ignore spaces, digits and punctuation. Treat uppercase and lowercase the same.
Examples
count_letters("Hello, World 123") → (3, 7)
count_letters("AEIOU")            → (5, 0)
count_letters("rhythm")           → (0, 6)
count_letters("")                 → (0, 0)
Constraints
Use a loop. No .count() and no .isalpha().
Decide if a character is a letter by comparing it between "a" and "z" after making it lowercase.
What this gauges: String iteration and keeping two counters at once.
"""

def count_letters(text):
    VOWELS = ('a', 'e', 'i', 'o', 'u')
    vowels = 0
    consonants = 0

    for ch in text:
        if 'a' <= ch.lower() <= 'z':
            if ch.lower() in VOWELS:
                vowels += 1 
            else:
                consonants += 1

    return vowels, consonants

print(count_letters("Hello, World 123"))
print(count_letters("AEIOU"))         
print(count_letters("rhythm"))           
print(count_letters(""))

