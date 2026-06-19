#Write a program to implement a linear search algorithm to find an element in an array.

array = list(map(int,input().split()))

target = int(input())
f = 0
for i in range (len(array)-1):
    if array[i] == target:
        f = 1
        break
    else:
       f = 01 2 3
if f == 1:
    print(f"Found at position {i}")
else:
    print("The element is not in the array")