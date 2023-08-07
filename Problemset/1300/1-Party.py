# https://codeforces.com/problemset/problem/1711/B
t = int(input())
for _ in range(t):
    n, m = list(map(int, input().split()))
    A = list(map(int, input().split()))
    S = []
    C = [0 for i in range(n + 1)]
    for i in range(m):
        x, y = list(map(int, input().split()))
        S.append(A[x - 1] + A[y - 1])
        C[x] += 1
        C[y] += 1
    if m % 2 == 0:
        print(0)
    else:
        L = []
        for i in range(1, n + 1):
            if C[i] % 2:
                L.append(A[i - 1])
        L.sort()
        S.sort()
        if L:
            print(min(L[0], S[0]))
        else:
            print(S[0])
