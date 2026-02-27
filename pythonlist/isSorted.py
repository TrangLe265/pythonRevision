# Check if an array is sorted
def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i] < arr[i+1]:
            return True
    return False

print(is_sorted([1,2,3]))

# this check for both ascending and descending
def is_sorted2(arr):
    ascending = all(arr[i] <= arr[i+1] for i in range(len(arr)-1))
    descending = all(arr[i] >= arr[i+1] for i in range(len(arr)-1))
    return ascending or descending

# another approach using sorted()
def is_sorted3(arr):
    return arr == sorted(arr) or arr == sorted(arr, reverse=True)
