#Write a program to print a message n times using recursion.
def display (n):
    if (n == 0):
        return
    
    print("Hello")
    display(n-1)

n = int(input())
display(n)
