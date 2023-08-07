# https://codeforces.com/problemset/problem/1712/C
for s in [*open(0)][2::2]:
    p = 0
    t = {0}
    q = {0}
    for x in map(int, s.split()):
        x *= x not in t
        if x < p:
            t |= q
            q = {0}
        q |= {x}
        p = x
    print(len(t) - 1)
