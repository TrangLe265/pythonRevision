"""
Given a dictionary, the task is to calculate the sum of all its values.
"""
def sum_of_values(dictionary):
    sum = 0
    for key in dictionary.keys():
        sum += dictionary.get(key)
    return sum

print(sum_of_values({'a': 100, 'b': 200, 'c': 300}))

# option 2: use built-in sum method
d = {'a': 100, 'b': 200, 'c': 300}
res = sum(d.values())
print(f"Using sum method: {res}")

