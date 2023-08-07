# https://codeforces.com/problemset/problem/469/A
n = int(input())
X = list(map(int, input().split()))
Y = list(map(int, input().split()))
X.pop(0)
Y.pop(0)
line = []
for i in X:
    line.append(i)
for i in Y:
    line.append(i)
line = list(set(line))
line.sort()
if len(line) == n:
    print("I become the guy.")
else:
    print("Oh, my keyboard!")
