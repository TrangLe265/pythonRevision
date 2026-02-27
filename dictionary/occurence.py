"""
Given a list of names, count how many times each name appears
"""
names = ["Alice", "Bob", "Alice", "Charlie", "Bob", "Alice", "David"]

names_count = {}
for name in names: 
    names_count[name] = names_count.get(name,0) + 1
#print(names_count)

"""
Given a sentence, count the frequency of each word (not character)
"""
sentence = "I think pasta is great but it is a bit fatty"
words = sentence.split(" ")
word_freq = {}
for word in words:
    word_freq[word.lower()] = word_freq.get(word.lower(), 0) + 1

print(word_freq)