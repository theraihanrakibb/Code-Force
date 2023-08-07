# https://codeforces.com/problemset/problem/266/B
n, x = map(int, input().split())
s = input()
for i in range(x):
    s = s.replace("BG", "GB")
print(s)
