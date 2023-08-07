# https://codeforces.com/problemset/problem/69/A
n = int(input())
x = y = z = 0
for i in range(n):
    x1, y1, z1 = [int(x) for x in input().split()]
    x += x1
    y += y1
    z += z1
if x == 0 and y == 0 and z == 0:
    print("YES")
else:
    print("NO")
