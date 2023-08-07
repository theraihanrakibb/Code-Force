# https://codeforces.com/problemset/problem/58/A
s = iter(input())
print('NYOE S'[all(c in s for c in 'hello')::2])
