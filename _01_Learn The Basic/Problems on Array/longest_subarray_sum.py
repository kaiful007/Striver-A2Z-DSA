"""Write a program to find the length of the longest subarray with sum equal to K,
     where the array contains both positive and negative integers.
        Example: Input: [1,-1, 5,-2, 3],K=3 
        Output: 4(subarray [1,-1, 5,-2])"""

array = list(map(int, input().split()))
k = int(input())

max_len = 0
start = 0
end = 0

for i in range(len(array)):
    total = 0

    for j in range(i, len(array)):
        total += array[j]

        if total == k:
            if j - i + 1 > max_len:
                max_len = j - i + 1
                start = i
                end = j

print("Sub-array =", end=" ")

for i in range(start, end + 1):
    print(array[i], end=" ")