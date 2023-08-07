# https://codeforces.com/problemset/problem/1700/B
def main():
    n = int(input())
    s = input()
    ans = []
    if s[0] == '9':
        p = 0
        for i in s[::-1]:
            i = int(i) + p
            if i == 1:
                ans.append('0')
                p = 0
            elif i == 0:
                ans.append('1')
                p = 0
            else:
                ans.append(str(11 - i))
                p = 1
        ans.reverse()
    else:
        for i in s:
            ans.append(str(9 - int(i)))
    print(''.join(ans))


for _ in range(int(input())):
    main()
