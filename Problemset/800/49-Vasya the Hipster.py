# https://codeforces.com/problemset/problem/581/A
a, b = map(int, input().split())
print(min(a, b), abs(a - b) // 2)
