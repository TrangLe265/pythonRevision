#You are given a number N, you need to print its multiplication table.

def multiplicationTable(N):
    output = []
    for n in range(1,11):
        output.append((N*n))
    print(*output)

multiplicationTable(42425)