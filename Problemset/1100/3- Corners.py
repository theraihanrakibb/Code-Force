# https://codeforces.com/problemset/problem/1720/C
t = int(input())

for i in range(t):
    n, m = [int(x) for x in input().split()]
    d = [list(map(int, input())) for x in range(n)]

    c = sum(sum(r) for r in d)
    perfect = False

    if c == n * m:
        print(c - 2)
    elif c == 0:
        print(0)
    else:
        for p in range(n - 1):
            for q in range(m - 1):
                s = d[p][q] + d[p][q + 1] + d[p + 1][q] + d[p + 1][q + 1]
                if s <= 2:
                    perfect = True
                    break
            if perfect: break

        print(c if perfect else c - 1)
