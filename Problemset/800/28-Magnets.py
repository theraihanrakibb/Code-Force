# https://codeforces.com/problemset/problem/344/A
n = int(input())
a = []
z = 0
for i in range(1, n + 1):
    a.append(input())
    if i > 1:
        if a[i - 1] != a[i - 2]:
            z += 1
print(z + 1)
