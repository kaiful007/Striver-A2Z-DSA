#Write a program to move all zeros in an array to the end without changing the order of non-zero elements.

array = list(map(int, input().split()))

j = 0

for i in range(len(array)):
    if array[i] != 0:
        array[j], array[i] = array[i], array[j]
        j += 1

print(array)