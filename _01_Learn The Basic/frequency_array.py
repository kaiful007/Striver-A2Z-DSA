arr = list(map(int, input().split()))

arr.sort()

count = 1

for i in range(len(arr) - 1):
    if arr[i] == arr[i + 1]:
        count += 1
    else:
        print(arr[i], count)
        count = 1

print(arr[-1], count)