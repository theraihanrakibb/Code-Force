# https://codeforces.com/problemset/problem/318/A
n, k = map(int, input().split())
if k <= n - n // 2:
    print(2 * k - 1)
else:
    k -= n - n // 2
    print(2 * k)
