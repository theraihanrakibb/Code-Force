# https://codeforces.com/problemset/problem/1708/B
for s in [*open(0)][1:]:
    n, l, r = map(int, s.split())
    f = min(a := [r - r % i for i in range(1, n + 1)]) >= l
    print('NYOE S'[f::2], *a * f)
