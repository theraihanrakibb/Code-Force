# https://codeforces.com/problemset/problem/677/A
# N, h, *a = map(int, open(0).read().split())
# print(N + sum(n > h for n in a))

num, fence = [int(x) for x in input().split()]
heights = [int(x) for x in input().split()]
road = 0

for i in heights:
    if i > fence:
        road += 2
    else:
        road += 1

print(road)
