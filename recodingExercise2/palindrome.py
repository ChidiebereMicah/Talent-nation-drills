def palindrome(word):
    for i in range(len(word)//2):
        if word[i] == word[len(word) - i - 1]:
            continue
        else:
            return "Not a palindrome"
    return "Palindrome"

word = input("Enter your word to check palindrome status: ")
print(palindrome(word))
