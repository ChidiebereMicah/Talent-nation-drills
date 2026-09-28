import sys

word1 = input("Enter 1st word for anagram match: ").lower()
word2 = input("Enter 2nd word for anagram match: ").lower()

def ch_freq_map(word):
    ch_freq = {}
    for ch in word:
        if ch not in ch_freq:
            ch_freq[ch] = 1
        else:
            ch_freq[ch] += 1
    return ch_freq

word1_map = ch_freq_map(word1)
word2_map = ch_freq_map(word2)

for key in word1_map:
    try:
        if word1_map[key] == word2_map[key]:
            continue
        else:
            print("Not an anagram")
            sys.exit(1)
    except KeyError as error:
        print("Not an anagram")
        sys.exit(1)
        
print("Anagram")

