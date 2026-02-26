"""
Given a string s, you need to check if it is palindrome or not. A palidrome is a string that reads the same from front and back.
"""

def check_palindrome(string):
    string = list(string.lower())
    reverse = list(reversed(string))
    if string == reverse:
        print("True")

check_palindrome("tenet")

"""
Given a string s, reverse the string without reversing its individual words. Words are separated by dots(.).
"""
def reverse_string(s):
    s = s.split('.')
    result = list(reversed(s))
    s_list = (e for e in result if e != '')
    return (".").join(s_list)

print(reverse_string("...i.like.this.program.very.much"))