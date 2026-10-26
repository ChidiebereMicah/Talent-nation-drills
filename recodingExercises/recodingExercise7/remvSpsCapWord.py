def remv_sps_cap_word(words):
    words = words.strip()
    words_list = words.split(" ")
    capitalized = ""
    for word in words_list:
        if 'a' < word[0] < 'z':
            word[0] = chr(ord(word[0]) - 32)
    capitalized = " ".join(words_list)
    no_space = ''.join(words_list)
    return(f"Capitalized: {capitalized}\n"
           f"No Spaces: {no_space}"
           )

    for i in range(len(words)):
        capitalized = ""
        if not i and 'a' < words[i] < 'z':
            capitalized +=


print(remv_sps_cap_word("hello world from python"))