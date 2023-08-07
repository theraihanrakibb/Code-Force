# https://codeforces.com/problemset/problem/271/A
Year = int(input()) + 1
while len(set(str(Year))) < 4:
    Year += 1
print(Year)
