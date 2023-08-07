# https://codeforces.com/problemset/problem/1725/A
n, m = map(int, input().split())
print(max(n - 1, n * (m - 1)))
