def print_triangle(n):
    for i in range(n,0,-1):
        print ('*'*i)

#print_triangle(5)§

"""Help Geek to build a star pattern."""
def print_star(n):
    for i in range(1,n,1):
        print ('*'*i)
    for i in range(n,0,-1):
        print ('*'*i)
    
print_star(5)