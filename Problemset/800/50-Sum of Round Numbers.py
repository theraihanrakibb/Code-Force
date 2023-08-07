# https://codeforces.com/problemset/problem/1352/A
t = int(input())

l = []

for i in range(t):
    l.append(int(input()))

for el in l:
    cnt = 0
    res = []

    a10 = 0

    while el > 0:
        if el % 10 != 0:
            res.append(str((el % 10) * (10 ** a10)))
            cnt += 1
        a10 += 1

        el //= 10

    print(cnt)
    print(' '.join(res))
