case = int(input())
for i in range(case):
    n = int(input())
    list1 = []
    print(n)
    for j in range(n):
        list1.append(str(j + 1))
    print(" ".join(list1))
    for k in range(n - 1):
        list1[k], list1[k + 1] = list1[k + 1], list1[k]
        print(" ".join(list1))
