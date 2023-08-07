# https://codeforces.com/problemset/problem/1703/D
for _ in range(int(input())):
    n = int(input())
    l = []
    s = ''
    for i in range(n):
        l.append(input())
    st = set(l)
    for i in l:
        for j in range(1, len(i)):
            if i[:j] in st and i[j:] in st:
                s += '1'
                break
        else:
            s += '0'
    print(s)
