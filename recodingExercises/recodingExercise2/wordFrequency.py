sentence = input("Enter your sentence: ")
sentence = sentence.lower().strip().split(" ")

word_freq = {}
for word in sentence:
    if word not in list(word_freq):
        word_freq[word] = 1
    else:
        word_freq[word] += 1
print(word_freq)