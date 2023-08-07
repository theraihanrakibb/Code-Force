# https://codeforces.com/problemset/problem/785/A
from sys import stdin, stdout

polyhedron = {'Tetrahedron': 4, 'Cube': 6, 'Octahedron': 8, 'Dodecahedron': 12, 'Icosahedron': 20}
n = int(stdin.readline())
total = 0
for i in range(n):
    total += polyhedron[stdin.readline().rstrip()]
stdout.write(str(total))

# i = input
# print(sum({'T': 4, 'C': 6, 'O': 8, 'D': 12, 'I': 20}[i()[0]] for _ in range(int(i()))))
