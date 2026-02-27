# Find all pairs in an array that sum to a target k
def find_pairs(k, arr):
    seen = set() #We will store all the number that has been looped in here
    result = []

    for num in arr: 
        remaining = k - num
        # check if the remainder or num is already tracked before inside of seen set
        # seen stores all the visited nums
        # if it does exist inside seen, then we found 1 suitable pair
        if remaining in seen:
            result.append((remaining,num))
        #if not in seen yet, then we add the current num into seen 
        seen.add(num)
    return result

print(find_pairs(4, [2,2,4,3,1,5,0]))