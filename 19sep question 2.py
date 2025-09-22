# Problem 2: Write a program that counts how many times each word appears in a given list using a dictionary.
words = ["apple", "banana", "apple", "orange", "banana", "apple"]
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print(word_count)
