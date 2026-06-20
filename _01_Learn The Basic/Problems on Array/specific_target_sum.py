#Write a program to find two numbers in an array that add up to a specific target sum.

array = list(map(int, input().split()))
target = int(input())

f = 0

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] + array[j] == target:
            print(i, j)
            f = 1
            break

    
if f == 0:
    print("Not found")