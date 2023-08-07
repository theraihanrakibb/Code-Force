# https://codeforces.com/problemset/problem/200/B
n = input()
p = input().split()

# convert each item to int type
for i in range(len(p)):
    # convert each item to int type
    p[i] = int(p[i])

# Calculating the sum of list elements
print(int(sum(p)) / int(n))

"""
n = int(input().strip())
p = list(map(int, input().strip().split(' ')))
Percentage = [x / n for x in p]
print(sum(Percentage))
"""