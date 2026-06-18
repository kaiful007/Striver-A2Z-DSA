#Write a program to check wheather a given integer is a prime number.
n = int(input())

f = 0

for i in range (2,n):
    if(n % i == 0):
        f = 1
        break
    else:
        f = 0

if(f == 1):
    print("Not a Prime Number")
else:
    print("Prime Number")