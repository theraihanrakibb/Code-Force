# https://codeforces.com/problemset/problem/734/A
n = int(input())
s = input()
Anton = s.count('A')
Danik = s.count('D')
if Anton > Danik:
    print("Anton")
if Danik > Anton:
    print("Danik")
if Anton == Danik:
    print("Friendship")
