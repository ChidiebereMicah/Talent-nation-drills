
def balanced_paren(text):
    count = 0
    for ch in text:
        if ch == '(':
            count += 1
        elif ch == ')':
            count -= 1
        if count < 0:
            return "Not Balanced"
        
    if count == 0:
        return "Balanced"
    return "Not Balanced"


print(balanced_paren("(a+b) * (c-d)"))
print(balanced_paren("(a+b))"))
print(balanced_paren("(a+b))("))
print("Test",balanced_paren("())(()"))


