# https://codeforces.com/problemset/problem/131/A
# n = input()
# print([n, n.swapcase()][n[1:].upper() == n[1:]])
string = input()
flag = True
for c in string[1:]:
    if c.islower():
        flag = False
        break
if flag:
    print(string.swapcase())
else:
    print(string)
