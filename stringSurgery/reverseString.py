def reverse_string(value):
    str_len = len(value)-1
    rev_str = ""
    for i in range(len(value)):
        rev_str = rev_str + value[str_len]
        str_len-=1

    return rev_str

print(reverse_string("abcde"))