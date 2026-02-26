"""Custom encoder
Write a function called "custom_encoder" that accepts a string text as parameter and for each char of the text it calculates its 0-based position in the following reference string:

reference_string = 'abcdefghijklmnopqrstuvwxyz'

The function should return a list that contains all the positions. If a char is not found in the reference_string, its position should be -1
"""

def custom_encoder(string):
    ref = list('abcdefghijklmnopqrstuvwxyz')
    string = string.lower()
    position = []
   
    for char in string:
        if char in ref:
            position.append(ref.index(char))
        else:
            position.append(-1)
    
    return position

print(custom_encoder('HollyWood'))