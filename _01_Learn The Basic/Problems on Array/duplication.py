#Write a program to remove duplicates from a sorted array and return the new length of the array with unique elements.

array = list(map(int, input().split()))

i = 1

while i < len(array):
    if array[i] == array[i - 1]:
        array.pop(i)
    else:
        i += 1

print("New Length =", len(array))
print(array)