#Write a program to left rotate an array by D places.

array = list(map(int, input().split()))

d = int(input())

n = len(array)

# Reverse first d elements
for i in range(d // 2):
    array[i], array[d - 1 - i] = array[d - 1 - i], array[i]

# Reverse remaining elements
for i in range((n - d) // 2):
    array[d + i], array[n - 1 - i] = array[n - 1 - i], array[d + i]

# Reverse entire array
for i in range(n // 2):
    array[i], array[n - 1 - i] = array[n - 1 - i], array[i]

print(array)