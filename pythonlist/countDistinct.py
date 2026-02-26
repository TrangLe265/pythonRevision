def countDistinct(arr):
        #code here 
    distinct = list(set(arr))
    print(distinct)
    return len(distinct)

print(countDistinct([2, 3, 4, 5, 1, 2, 14, 6, 8, 7, 5]))
