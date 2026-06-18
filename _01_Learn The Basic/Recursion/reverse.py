#Write a program to Reverse an array using Recursion.

def reverse_array(arr, left, right):
    if left >= right:
        return

    arr[left], arr[right] = arr[right], arr[left]

    reverse_array(arr, left + 1, right - 1)


n = int(input())
arr = list(map(int, input().split()))

reverse_array(arr, 0, n - 1)

print(arr)
