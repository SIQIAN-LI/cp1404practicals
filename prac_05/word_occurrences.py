"""
Word Occurrences
Estimate: 20 minutes
Actual:   15 minutes
"""
text = input("Text: ")
words = text.split()
word_to_count = {}
for word in words:
    frequency = word_to_count.get(word, 0)
    word_to_count[word] = frequency + 1
print(word_to_count)

