#Write a program to find the Nth fibonacci number usig recursion.

def fibonacci (n,first, second):
    if n == 0:
        return first
    

    return fibonacci(n-1, second, first+second)

first = 0
second = 1
n = int(input())
print(fibonacci(n,first,second))


