# https://codeforces.com/problemset/problem/41/A
# print('YNEOS'[input() != input()[::-1]::2])
s = input()
t = input()
if s[::-1] == t:  # Reverse the sting s.
    print('YES')
else:
    print('NO')
