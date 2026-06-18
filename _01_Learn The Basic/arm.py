#Write a program to check a given integer is an Armstrong Number

n = int(input())
copy = n
real = n
count = 0
sum = 0

while (n != 0):
    digit = n%10
    count += 1
    n //= 10

while(copy > 0):
    digit = copy % 10
    sum = sum + digit ** count
    copy //= 10
if(sum == real):
    print("Armstrong Number")
else:
    print("Not an armstrong Number")


