# https://codeforces.com/problemset/problem/160/A
n = int(input())
a = list(map(int, input().split()))

x = 0
y = sum(a)

a.sort(reverse=True)
for i in range(n):
    x += a[i]
    y -= a[i]

    if x > y:
        print(i + 1)
        break
