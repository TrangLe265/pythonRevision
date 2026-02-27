"""
Find the first non-repeating character in a string
"""
string = "I am so tired of applying for jobs"
string = string.replace(" ","").lower()
frequency = {}
for char in string:
    frequency[char] = frequency.get(char, 0) + 1

for key in frequency.keys(): #this only works with python 3.7 and above
    if frequency[key] == 1:
        print(key)
        break