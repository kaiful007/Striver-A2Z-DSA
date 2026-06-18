#Write a program to find the sum of first N natural numbers using recursion.

def sum_of_N_Natural_Number(n, sum):
    if n == 0:
        return sum

    sum = sum + n
    return sum_of_N_Natural_Number(n - 1, sum)

n = int(input())
sum = 0
print(sum_of_N_Natural_Number(n, sum))