"""
Count vowels
Assume s is a string of lower case characters.
Write a program that counts up the number of vowels contained in the string s. Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

For example, if s = 'hello', your program should print:

Number of vowels: 2

The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:
For example:

Input	Result
Restaurant
Number of vowels: 4
Air
Number of vowels: 2

"""
def count_vowel(Input):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    
    for char in Input:
        if char.lower() in vowels:
            count +=1
    
    print(f"Number of vowels: {count}")

count_vowel("Air")