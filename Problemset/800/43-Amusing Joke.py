# https://codeforces.com/problemset/problem/141/A
a, b, c = input(), input(), input()
if sorted(a + b) == sorted(c):
    print("YES")
else:
    print("NO")
