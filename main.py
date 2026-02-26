# Custom function to be applied
# in map
def double(val):
    return val * 2

# Let us apply double on every member
a = [0,10] 
res = list(map(lambda x : x *2, a))
print(res)