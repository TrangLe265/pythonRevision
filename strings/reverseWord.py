"""
Reverse each word in a sentence individually
"""
sentence = "Hips dont lie"
words = sentence.split(" ")
result = []
for word in words: 
    result.append(word[::-1]) 

#print(result)

#even shorter: 
result2 = " ".join(word[::-1] for word in sentence.split())
print(result2)