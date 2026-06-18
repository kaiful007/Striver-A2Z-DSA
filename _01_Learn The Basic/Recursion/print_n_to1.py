#Write a program to print number from N to 1.

def print_from_N_to_1(n):
    if(n == 0):
        return 
    
    print(n)
    print_from_N_to_1(n-1)

n = int(input())
print_from_N_to_1(n)
