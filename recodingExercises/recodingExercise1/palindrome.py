def palindrome(word):
    for index in range(len(word)//2):
        if word[index] == word[len(word) - index - 1]:
            continue
        else:
            return f"{word} is not a palindrome"
    return f"{word} is a palindrome"

word = input("Enter your word for palindrome test: ")
print(palindrome(word))



