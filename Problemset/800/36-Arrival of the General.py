# https://codeforces.com/problemset/problem/144/A
n = int(input())
a = [*map(int, input().split())]
b = a.index(max(a)) + a[::-1].index(min(a))
print(b - (b >= n))
