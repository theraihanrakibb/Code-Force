# https://codeforces.com/problemset/problem/617/A
x = int(input())

ans = int(x / 5)

if x % 5 > 0:
    ans = ans + 1

print(ans)
