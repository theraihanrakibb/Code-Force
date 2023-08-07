# https://codeforces.com/problemset/problem/580/A
t = int(input())

l = list(map(int, input().split()))
c = 1
ans = 1
for i in range(t - 1):
    if l[i] <= l[i + 1]:
        c = c + 1
    else:
        ans = max(c, ans)
        c = 1
ans = max(c, ans)
print(ans)
