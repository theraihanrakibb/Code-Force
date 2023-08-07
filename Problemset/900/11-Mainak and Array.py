# https://codeforces.com/problemset/problem/1726/A
for i in range(int(input())):
    n = int(input())
    ls = [int(j) for j in input().split()]
    ans = 0

    for x in range(n):
        ans = max([ans, ls[x] - ls[0], ls[n - 1] - ls[x], ls[x] - ls[(x + 1) % n]])
    print(ans)
