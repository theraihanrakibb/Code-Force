# https://codeforces.com/problemset/problem/1760/C
for s in [*open(0)][2::2]:
    a = *map(int, s.split()),
    b = sorted(a)
    print(*(x - b[~(x == b[-1])] for x in a))
