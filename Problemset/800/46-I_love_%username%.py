# https://codeforces.com/problemset/problem/155/A
n = input()
high, low = 0, 0
res = 0
for i, p in enumerate(list(map(int, input().split()))):
    if i == 0:
        high = low = p
    if p > high:
        high = p
        res += 1
    if p < low:
        low = p
        res += 1
print(res)
