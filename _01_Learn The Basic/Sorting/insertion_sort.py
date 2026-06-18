""""Write a program to implement Insertion Sort. 
    Insertion Sort works by picking elements one by one and placing them in their 
        correct position in the sorted part of the array."""

array = list(map(int, input().split()))

for i in range(1, len(array)):
    j = i
    while j > 0 and array[j - 1] > array[j]:
        array[j - 1], array[j] = array[j], array[j - 1]
        j -= 1

print(array)