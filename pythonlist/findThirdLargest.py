#Given a list of positive integer, find third largest
def third_largest(nums):
    first,second, third = float('-inf'),float('-inf'),float('-inf')
    
    for num in nums:
        if num > first:
            third = second
            second = first
            first = num
        elif num > second:
            third = second
            second = num
        elif num > third:
            third = num
    
    return third if third != float('-inf') else None

print(third_largest([855 ,450, 132 ,359 ,233 ,825 ,604 ,481,262 ,337 ,720, 525, 652 ,300 ,906, 219 ,926 ,906 ,293 ,864 ,817 ,498 ,30 ,639 ,661]))