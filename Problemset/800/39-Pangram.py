# https://codeforces.com/problemset/problem/520/A
n = input()
letter = len(set(input().upper()))

if letter == 26:
    print("YES")
else:
    print("NO")

# input(), print('YNEOS'[len(set(input().upper())) < 26::2])
