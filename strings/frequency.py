"""
Given a string, the task is to identify the character that appears the least number of times. For example, in "GeeksforGeeks", the character 'f' occurs only once, so it is the least frequent.
"""

def frequency_by_dict(s):
    freq = {}
    for char in s.lower():
        freq[char] = freq.get(char,0) + 1
    
    res = min(freq, key=freq.get )
    print(str(res))

frequency_by_dict("GeeksforGeeks")