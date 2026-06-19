#Write a program to find the maximum number of consecutive 1's in a binary array.

array = list(map(int,input().split()))

count = 0
max_count = 0
for i in range(len(array)):
    if array[i] == 1:
        count += 1
    else:
        if max_count < count:
            max_count = count
            count = 0
        else:
            count = 0
print(max_count)