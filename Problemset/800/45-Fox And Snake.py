# https://codeforces.com/problemset/problem/510/A
n, m = map(int, input().split())
a = "#" * m
b = "." * (m - 1) + "#"
for i in range(n):
    if i % 2 == 0:
        print(a)
    else:
        print(b)
        b = b[::-1]
