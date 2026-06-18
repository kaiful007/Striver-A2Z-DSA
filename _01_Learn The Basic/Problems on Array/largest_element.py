#Write a program to find the largest element in a given array.

array = list(map(int,input().split()))

max = 0

for i in range(len(array)):
    if (array[max] < array[i]):
        max = i

print(array[max])