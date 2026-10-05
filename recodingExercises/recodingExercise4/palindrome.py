def palindrome(text):
    text = text.lower()
    clean_text = ""
    for ch in text:
        if ch.isalpha():
            clean_text += ch
    for i in range(len(clean_text)-1//2):
        if clean_text[i] == clean_text[len(clean_text)-1-i]:
            continue
        else:
            return "Not a palindrome"

    return "Palindrome"

# def _palindrome(text, left, right):
#     if text[left] == text[right]:

#         _palindrome()

text = input("Please enter your text: ")
print(palindrome(text))
