"""
The hiring team aims to find 3 candidates who are great collectively. Each candidate has his or her ability expressed as an integer. 3 candidates are great collectively if the product of their abilities is maximum. Given the abilities of some candidates in an array, arr[], return the maximum collective ability from the pool of candidates.
"""
def maxProduct(arr):
    #in math multiplication, sign matters a lot
    """The maximum product of three numbers must come from either:
    1️⃣ The three largest numbers""
    2️⃣ The two smallest numbers (most negative) × the largest number"""

    n = len(arr)
    
    # Initialize Maximum, second maximum 
    # and third maximum element
    maxA = float('-inf') #largest
    maxB = float('-inf') #secondLargest
    maxC = float('-inf')   #thirdlargest

    for num in arr:
        if num > maxA:
            maxC = maxB
            maxB = maxA
            maxA = num
        elif num > maxB:
            maxC = maxB
            maxB = num
        elif num > maxC:
            maxC = num

    minA = float('inf') #smallest
    minB = float('inf') #2ndsmallest

    for num in arr:
        if num < minA:
            minB = minA 
            minA = num
        elif num < minB:
            minB = num

    return max(maxA*maxB*maxC,
               minA*minB*maxA)

    
print(maxProduct([852, -566, 182, -638, -693, -323]))