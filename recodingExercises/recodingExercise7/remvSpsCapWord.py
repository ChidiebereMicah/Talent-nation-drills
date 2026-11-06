"""
5. Remove Spaces & Capitalize Words

Suggested time: 15–20 minutes

Problem
Given a sentence, capitalize the first letter of every word, then create a second version with all spaces removed.
Examples
Input: "hello world from python"
Capitalized: "Hello World From Python"
No Spaces: "HelloWorldFromPython"
Constraints
Do not use .replace() to remove spaces.
Do not use .title() or .capitalize().
Use loops and conditionals.
Use ASCII logic to capitalize the first letter (check if the character is between 'a' and 'z', and convert it by subtracting 32 from its ASCII value using ord() and chr()).
Do not import libraries.
What This Tests: String manipulation, ASCII codes (ord/chr), loops, and flags that track the start of a word.

"""

def remv_sps_cap_word(words):
    if not words.strip():
        return words
    
    words_list = words.strip().split()

    cap_list = []
    for word in words_list:
        cap_word = word
        if 'a' <= word[0] <= 'z':
            cap_word = chr(ord(word[0]) - 32) + word[1::]
        cap_list.append(cap_word)
    capitalized = " ".join(cap_list)
    no_space = ''.join(cap_list)
    return(f"Capitalized: {capitalized}\n"
           f"No Spaces: {no_space}"
           )

def remv_sps_cap_word(words):
    capitalized = []
    at_first_ch = True
    for ch in words:
        if ch == " ":
            capitalized.append(ch)
            at_first_ch = True
            continue

        if at_first_ch and 'a' <= ch <= 'z':
            capitalized.append(chr(ord(ch)-32))
        else:
            capitalized.append(ch)
        at_first_ch = False

    return(f"Capitalized: {''.join(capitalized)}\n"
            f"No Spaces: {''.join(ch for ch in capitalized if ch != ' ')}"
    )


print(remv_sps_cap_word("hello world from python"))
print(remv_sps_cap_word(" "))


