"""
Sort characters
Write a program that takes a single string as its input and sort its characters from the lowest Unicode value to the highest Unicode value. The program should print the new string.
The output from your program, when called with the code in the Test column, should be exactly as shown in the Result column:
Input	Result
wikipedia adeiiikpw
assume aemssu
"""
def sort_char(word):
 result= ''.join(sorted(word))
 print(result)
    
sort_char("assume")

def sort_char_v2(word):
 sorted = list(word)

 for i in range(len(sorted)):
  for j in range(i+1,len(sorted)):
   if ord(sorted[i]) > ord(sorted[j]):
    sorted[i], sorted[j] = sorted[j],sorted[i]

 print(''.join(sorted))

sort_char_v2("assume")


