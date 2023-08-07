# https://codeforces.com/problemset/problem/1713/C
# import math
#
#
# def solve(n):
#     x = math.sqrt(n)
#     if int(x) == x:
#         for i in range(n, -1, -1):
#             print(i, end=' ')
#     else:
#         y = math.ceil(x)
#         y = y * y - n
#         solve(y - 1)
#         for j in range(n, y - 1, -1):
#             print(j, end=' ')
#
#
# for _ in range(int(input())):
#     n = int(input())
#     solve(n - 1)
#     print()

n = int(input())
ans = []
for _ in range(n):
    n = int(input())
    a = [0] * n
    p = n - 1
    while p >= 0:
        i = 0
        while i * i < p:
            i += 1
        l = i * i - p
        for k in range(l, p + 1):
            a[k] = p + l - k
        p = l - 1
    ans.append(a)
for i in ans:
    print(*i)
