#Write a program to find the missing number in a given array of integers from 1 to N.

array = list(map(int,input().split()))
for i in range(len(array)):
    if array[i] != i + 1:
        print(i + 1)
        break