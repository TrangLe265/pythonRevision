def findUnion(a, b):
    distinct_a = set(a)
    distinct_b = set(b)
    union = distinct_a.union(distinct_b)
    return list(union)

print()