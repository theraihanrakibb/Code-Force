# https://codeforces.com/problemset/problem/1335/A
t = int(input())
arr = []
for i in range(t):
    n = int(input())
    arr.append(n)
for ele in arr:
    if ele % 2 == 1:
        print((ele - 1) // 2)
    else:
        print((ele - 2) // 2)
