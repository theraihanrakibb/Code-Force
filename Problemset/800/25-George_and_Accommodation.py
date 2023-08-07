# https://codeforces.com/problemset/problem/467/A
x = int(input())
count = 0
for i in range(x):
    lst1 = list(map(int, input().split()))
    if (lst1[1] - lst1[0]) >= 2:
        count += 1
print(count)
