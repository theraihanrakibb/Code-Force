# https://codeforces.com/problemset/problem/136/A
Quantity = int(input())
n = input().split()
for i in range(Quantity):
    print(n.index(str(i+1))+1, end=' ')

# print(*[n.index(str(i+1))+1 for i in range(Quantity)])
