# https://codeforces.com/problemset/problem/1706/B
for s in [*open(0)][2::2]:
    a = s.split()
    r = [[0, 0] for _ in a]
    i = 0
    for x in a:
        x = int(x) - 1
        r[x][i & 1] = r[x][~i & 1] + 1
        i += 1
    print(*map(max, r))
