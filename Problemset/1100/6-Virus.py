# https://codeforces.com/problemset/problem/1704/C
for _ in range(int(input())):
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    lg = [a[i + 1] - a[i] - 1 for i in range(m - 1)]
    lg.append(n - (a[-1] - a[0] + 1))
    lg.sort(reverse=True)
    ct = 1
    ans = 0
    for x in lg:
        if x - ct <= 0:
            ans += (x - ct == 0)
            break
        else:
            ans += x - ct
            ct += 4
    print(n - ans)
