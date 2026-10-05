def count_words(text) -> dict[str, int]:
    text = text.lower().strip().split(" ")
    for i in range(len(text)):
        clean_text = ""
        for ch in text[i]:
            if ch.isalpha() or ch.isdigit() or ch == " ":
                clean_text += ch
        text[i] = clean_text

    word_freq = {}
    for word in text:
        if word not in list(word_freq):
            word_freq[word] = 1
        else:
            word_freq[word] += 1
    return word_freq

def most_frequent(freq) -> str:
    most_freq = 0
    freq_word = ""
    for word in freq:
        if freq[word] > most_freq:
            most_freq = freq[word]
            freq_word = word
    return f"Most frequent word: {freq_word} ({freq[freq_word]})"

text = input("Please enter your text: ")
print((count_words(text)))
print(most_frequent((count_words(text))))