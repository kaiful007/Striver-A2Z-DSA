#Write a program to print a name N times using recursion
def print_name(n, name):
    if(n == 0):
        return 
    
    print(name)
    print_name(n-1,name)


a = int(input())
n = str(input())

print_name(a,n)

    