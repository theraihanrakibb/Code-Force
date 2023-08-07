# https://codeforces.com/problemset/problem/313/A
n = int(input())
print(max(n, int(n / 10), int(n / 100) * 10 - (-n) % 10))
