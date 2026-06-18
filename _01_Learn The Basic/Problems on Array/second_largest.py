# Write a program to find the second largest element in a given array without .

array = list(map(int,input().split()))

max = 0
second_max = 1

for i in range (len(array)):
    if array[i] > array [max]:
        second_max = max
        max = i    

print(array[second_max])
print(array[max])