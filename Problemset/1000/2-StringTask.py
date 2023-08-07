# https://codeforces.com/problemset/problem/118/A
# n = input().lower()
# for i in n:
#     if i not in 'aoyiue':
#         print('.', i, sep='', end='')
user_input = input().lower()
vowels = ["a", "e", "i", "o", "u", "y"]
output = ""
for alphabet in user_input:
    if alphabet not in vowels:
        output = output + "." + alphabet

print(output)
