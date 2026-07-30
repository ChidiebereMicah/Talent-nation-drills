"""CensorWords
Instructions
Implement censor_words(text, banned_word). 
Return a new string where every occurrence of banned_word is replaced with "***". 
The match is case-sensitive. Do not use import or regular expressions.
"""
#Simple Pythonic Solution
def censor_words(text, banned_word):
    return text.replace(banned_word, "***")

#Algorithmic Solution
def censor_words(text, banned_word):
    text_list = text.split()
    new_str = ""
    blocker = "***"

    for i in range(len(text_list)):     
        if i == len(text_list) - 1:
            if text_list[i] == banned_word:
                new_str = new_str + blocker
            else:
                new_str = new_str + text_list[i]
        else:
            if text_list[i] == banned_word:
                new_str = new_str + blocker + " "
            else:
                new_str = new_str + text_list[i] + " "
   
    return new_str

print(censor_words("spam spam eggs", "spam"))
print(censor_words("This code is bad", "bad"))