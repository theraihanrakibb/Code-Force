# https://codeforces.com/problemset/problem/996/A
# n = int(input())
# print(n // 100 + n % 100 // 20 + n % 20 // 10 + n % 10 // 5 + n % 5)

n = int(input())
bills = [100, 20, 10, 5, 1]
count = 0
for bill in bills:
    count += n // bill
    n %= bill
print(count)
