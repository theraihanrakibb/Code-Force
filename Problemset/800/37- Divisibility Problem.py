# https://codeforces.com/problemset/problem/1328/A
t = int(input())
a = []
for x in range(t):
    b = input().split()
    b = [int(i) for i in b]
    if b[0] % b[1] != 0:
        a.append(b[1] - (b[0] % b[1]))
    else:
        a.append(0)
for x in a:
    print(x)
