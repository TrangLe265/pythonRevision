#Group a list of words by their first letter
words = ["angle", "pasta", "meat", "medium"]
groups = {}
for word in words:
    first_letter = word[0]
    groups.setdefault(first_letter, []).append(word)

#group a list of words by their length
groups2 = {}
for word in words:
    length = len(word)
    groups2.setdefault(length, []).append(word)
print(groups2)
