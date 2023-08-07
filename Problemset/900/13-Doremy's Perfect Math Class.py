# https://codeforces.com/contest/1764/problem/B
import math

for s in [*open(0)][2::2]:
    d = 0
    for x in map(int, s.split()):
        d = math.gcd(d, x)
    print(x // d)
