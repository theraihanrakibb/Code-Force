# https://codeforces.com/problemset/problem/337/A
n, m = input().split()
n, m = int(n), int(m)
k = 0
lst = sorted(list(map(int, input().split())))
l = len(lst)
ans = []
while k <= l - n:
    a = lst[k:k + n]
    ans.append(a[-1] - a[0])
    k += 1
print(min(ans))
