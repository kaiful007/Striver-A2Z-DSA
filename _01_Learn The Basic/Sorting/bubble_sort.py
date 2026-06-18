""""Write a program to implement Bubble Sort. 
    Bubble Sort repeatedly steps through the list, compares adjacent elements, 
        and swaps them if they are in the wrong order. The process is repeated until the array is sorted."""
array = list(map(int,input().split()))

for i in range(len(array)-1):
    for j in range(i+1,len(array)):
        if array[i] > array[j]:
            array[i], array[j] = array[j], array[i]


print(array)