# check if two strings are anagram
def is_anagram(s1,s2):
    return sorted(s1.lower()) == sorted(s2.lower())

print(is_anagram("man", "na"))

from collections import Counter
def is_anagram2(s1,s2):
    return Counter(s1.lower()) == Counter(s2.lower())
print(is_anagram2("man", "na"))