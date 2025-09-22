# Problem 5: Given a list of words, group them in a dictionary where the key is the first letter and the value is a list of words starting with that letter.
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
grouped_words = {}

for word in words:
    first_letter = word[0].lower()
    if first_letter not in grouped_words:
        grouped_words[first_letter] = []
    grouped_words[first_letter].append(word)

print(grouped_words)
