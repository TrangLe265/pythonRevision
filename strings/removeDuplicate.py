# remove duplicate char from a word
def remove_duplicate(s):
    seen = set()
    result = []
    for char in s:
        if char not in seen: 
            seen.add(char)
            result.append(char)
    
    return "".join(result)

print(remove_duplicate("Freeting !"))

# remove duplicate word from a sentence
def rmv_word(sentence):
    seen = set()
    result = []
    for word in sentence.split(" "):
        if word not in seen:
            seen.add(word)
            result.append(word)
    
    return " ".join(seen)
print(rmv_word("Hi Hi helo"))