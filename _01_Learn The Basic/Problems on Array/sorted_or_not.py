# Write a program to check if a given array is sorted in non-decreasing order.

array = list(map(int,input().split()))

isSorted = 0
for i in range (len(array)-1):
    if array[i] > array[i+1]:
        isSorted = 1
        break
    else:
        isSorted = 0

if isSorted == 1:
    print ("Not Sorted in non-decreasing order.")
else:
    print("Sorted sorted in non-decreasing order.")