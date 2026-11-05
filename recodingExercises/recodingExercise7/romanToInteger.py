def romanToInt(s: str) -> int:
    roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    arabic = 0

    invert = False

    for i in range(len(s)):
        if s[i] not in roman:
            return "Invalid input"
        if i != len(s)-1 and roman[s[i]] < roman[s[i+1]]:
            arabic -= roman[s[i]]
        else:
            arabic += roman[s[i]]

    return arabic

s = "III"
q = "MCMXCIV"
print(romanToInt(s))
print(romanToInt(q))