"""
8. Run-Length Encoding

Suggested time: 20–25 minutes

Problem
Given a string, compress it using run-length encoding: replace consecutive repeated characters with the character followed by the count.
Examples
Input: "aaabbc" → a3b2c1
Input: "abcd" → a1b1c1d1
Input: "aaa" → a3
Input: "aabbaa" → a2b2a2
Constraints
Use a loop to walk through the string character by character.
Do not use itertools.groupby().
Do not import libraries.
Build the result string manually (using + or a list of parts joined at the end).
Do not hardcode the answer.
Handle uppercase and lowercase as distinct characters.
What This Tests: Strings, loops, state tracking, string building, and multi-step problem solving.
Optional Stretch: Write a second function that decodes a run-length encoded string back to the original, e.g. "a3b2c1" → "aaabbc". Handle multi-digit counts like "a12b2" correctly.

"""

def run_length_encoding(text):
    result = ""
    count = 1
    for i in range(len(text)):
        if i != len(text) - 1 and text[i] == text[i+1]:
            count += 1
        else:
            result += text[i] + str(count)
            count = 1
        
    return result

input1 = "aaabbc"
input2 = "abcd"
input3 = "aaa"
input4 = "aabbaa"
input5 = ""
print(run_length_encoding(input1))
print(run_length_encoding(input2))
print(run_length_encoding(input3))
print(run_length_encoding(input4))
print(run_length_encoding(input5))

#Optional stretch
def run_length_decoding(text):
    if not text:
        return ""
    ch = text[0]
    count = ""
    result = ""
    for i in range(1, len(text)):
        try:
            if i == len(text) - 1:
                count += text[i]
                result += ch*int(count)
            else:
                int(text[i])
                count += text[i]
        except ValueError:
            result += ch*int(count)
            ch = text[i]
            count = ""

    return result

input1 = "a3b2c1"
input2 = "a12b2"
input3 = ""
print(run_length_decoding(input1))
print(run_length_decoding(input2))
print(run_length_decoding(input3))


