#Write a program to check wheather a given integer is a palindrome

n = int(input())
copy = n
reverse = 0
while (n > 0):
    digit = n%10
    reverse = (reverse*10) + (digit)
    n //= 10

if copy == reverse:
    print("Palindrome")
else:
    print("Not palindrome")

