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
    ch = text[i]
    count = ""
    result = ""
    for i in range(1, len(text)):
        try:
            int(text[i])
            count += text[i]
        except ValueError:
            ch = text[i]
            result += text[i-1]*int(count)
            continue

