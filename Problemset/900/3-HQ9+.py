# https://codeforces.com/problemset/problem/133/A
s = input()
for c in s:
    if c in ['H', 'Q', '9']:
        print('YES')
        break
else:
    print('NO')
