#Write a program to left rotate an array by one place.

array = list(map(int, input().split()))

first = array[0]

for i in range(len(array) - 1):
    array[i] = array[i + 1]

array[-1] = first

print(array)