# https://codeforces.com/problemset/problem/339/B
a = 1
ans = 0
k, n = map(int, input().split())
l = list(map(int, input().split()))
for i in l:
    ans += (i - a) % k
    a = i
print(ans)
