#Write a program to find the union of two arrays.

array1 = list(map(int,input().split()))
array2 = list(map(int,input().split()))
array3 = []
for i in range (len(array1)):
    if array1[i] not in array3:
        array3.append(array1[i])
for i in range(len(array2)):
    if array2[i] not in array3:
        array3.append(array2[i])

print(array3)