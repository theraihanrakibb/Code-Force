# https://codeforces.com/problemset/problem/110/A
# n = input()
# print(['NO', 'YES'][(n.count('4') + n.count('7')) in [4, 7]])
n = input()

x = n.count('4') + n.count('7')

if x == 4 or x == 7:
    print('YES')
else:
    print("NO")
    