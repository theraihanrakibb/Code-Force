n = int(input())
Line = []
for i in range(n):
    if i % 2 != 0:
        Line.append("I love")
    else:
        Line.append("I hate")

print((" that ".join(Line)) + " it")
