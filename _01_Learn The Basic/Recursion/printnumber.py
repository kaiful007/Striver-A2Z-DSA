#Write a program to print 1 to N using recursion
def print_number(n,i):
    
    if(n == 0):
        return
    print(i)
    print_number(n-1,i+1)

n = int(input())
i = 1
print_number(n,i)
