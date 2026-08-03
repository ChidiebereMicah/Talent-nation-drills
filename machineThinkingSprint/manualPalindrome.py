"""
ManualPalindrome
Instructions

Implement manual_palindrome(text). 
Ignore spaces and letter case. 
Return true if the cleaned text reads the same forward and backward, 
otherwise return false. Do not use slicing shorthand or reversed. 
Students may need to research manual string reversal.
"""

def manual_palindrome(text):
    text = text.lower().replace(" ", "")
    count = len(text)
    reverse = ""
    for i in range(len(text)):
        reverse += text[count-1] 
        count -= 1

    return True if reverse == text else False

#better solution
def manual_palindrome(text):
    text = text.lower().replace(" ", "")
    for i in range(len(text) - 1, -1, -1):
        reverse += text[i]

    return reverse == text

#even more efficient because of the potential for early termination of the loop
def manual_palindrome(text):
    text = text.lower().replace(" ", "")
    left = 0
    right = len(text)-1

    while left < right:

        if text[left] != text[right]:
            return False

        left += 1
        right -= 1

    return True


print(manual_palindrome("Level"))