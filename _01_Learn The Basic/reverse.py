#Write a program to reverse a given integer
n = int(input())
reverse = 0
while (n > 0):
    digit = n%10
    reverse = (reverse*10) + (digit)
    n //= 10

print(reverse)