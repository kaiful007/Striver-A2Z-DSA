# Write a program to implement Selection Sort.
"""Selection Sort works by repeatedly finding the minimum element from the
        unsorted part of the array and placing it at the beginning."""

array = list(map(int, input().split()))

for i in range(len(array) - 1):
    for j in range(i + 1, len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]

print(array)