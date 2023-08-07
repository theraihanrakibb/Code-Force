# https://codeforces.com/problemset/problem/427/A
n = int(input())
l = list(map(int, input().split()))
p = 0
f = 0
for i in l:
    if i < 0 and p == 0:
        f = f - i
    elif i < 0 < p:
        p = p + i
    elif i > 0:
        p = p + i
print(f)
