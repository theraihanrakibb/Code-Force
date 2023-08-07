# https://codeforces.com/problemset/problem/230/A
s, n = map(int, input().split())
D = []
for i in range(n):
    a, b = map(int, input().split())
    D.append([a, b])

D.sort()
done = False
for i in range(n):
    if s > D[i][0]:
        s += D[i][1]
    else:
        print("NO")
        done = True
        break
if not done:
    print("YES")
