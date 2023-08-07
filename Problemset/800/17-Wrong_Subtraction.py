# https://codeforces.com/problemset/problem/977/A
n, k = map(int, input().split())
for i in [0] * k:
    n = [n // 10, n - 1][n % 10 > 0]
print(n)
