# https://codeforces.com/problemset/problem/405/A
num_columns = int(input())
num_cubes = list(map(int, input().split()))
num_cubes.sort()
for num in num_cubes:
    print(num, end=" ")
