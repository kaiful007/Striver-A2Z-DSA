#Write a program to find the greatest common divisor or highest common factor of two number

a = int(input())
b = int(input())

gcd = 1

for i in range(1, min(a, b)+1):
    if a % i == 0 and b % i == 0:
        gcd = i

print(gcd)