# https://codeforces.com/problemset/problem/61/A

# i = input
# print(''.join('01'[a != b] for a, b in zip(i(), i())))
s1 = input()
s2 = input()

s = ""
for i in range(len(s1)):
    if s1[i] == s2[i]:
        s = s + "0"
    else:
        s = s + "1"
print(s)
