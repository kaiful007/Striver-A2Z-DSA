#Write a program to find the element that appears only once in an array, where all other elements appear twice.

array = list(map(int,input().split()))

array.sort()
f = 0
for i in range(0,len(array)-1,2):
    if array[i] != array[i+1]:
        f = 1
        break

    else:
       f = 0
if f == 0:
    print(array[-1])
else:
    print(array[i])
