"""Write a Java program to find two numbers in an array that add up to a specific target sum. 
    Example:Input: [2, 7, 11, 15], target = 9   
    Output: [2, 7]"""



array = list(map(int, input().split()))
target = int(input())

found = 0

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] + array[j] == target:
            print([array[i], array[j]])
            found = 1
            break

    if found == 1:
        break

if found == 0:
    print("Not found")