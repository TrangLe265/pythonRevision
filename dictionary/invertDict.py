dict = {"a":1,"b":3,"c":4}

inverted = {}

for key,val in dict.items():
    inverted[val] = key
print(inverted)