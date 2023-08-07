# https://codeforces.com/problemset/problem/116/A
stops = int(input())
maxCapacity = 0
currentCapacity = 0
for i in range(0, stops):
    data = input().split(' ')
    currentCapacity -= int(data[0])
    currentCapacity += int(data[1])
    maxCapacity = max(maxCapacity, currentCapacity)
print(maxCapacity)
