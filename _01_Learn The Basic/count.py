#Write a program to count the number or digits of a given integer
n = int(input())
count = 0

while (n != 0):
    digit = n%10
    count += 1
    n //= 10

print (count)