for _ in range(int(input())):
    c = int(input())

    a = [list(map(int, input().split())) for _ in range(2)]
    a[0][0] = -1

    pos = (0, 0)

    dync = [0 for _ in range(c)]
    y = 0
    for x in range(c - 1):
        y = not y
        curr = max(a[y][x] + 2, a[y][x + 1] + 1)
        dync[x + 1] = max(curr, dync[x] + 2)

    top = list(range(0, c, 2))
    latestTime = 0
    for x in top[::-1]:
        dist = (c - x) * 2 - 1
        if x + 1 < c:
            curr = max(a[0][x] + dist + 1, a[0][x + 1] + dist, a[1][x] + 1, a[1][x + 1] + 2)
        else:
            curr = max(a[0][x] + 2, a[1][x] + 1)
        latestTime = max(latestTime + 2, curr)
        dync[x] = max(dync[x] + dist, latestTime)

    bottom = list(range(1, c, 2))
    latestTime = 0
    for x in bottom[::-1]:
        dist = (c - x) * 2 - 1
        if x + 1 < c:
            curr = max(a[1][x] + dist + 1, a[1][x + 1] + dist, a[0][x] + 1, a[0][x + 1] + 2)
        else:
            curr = max(a[1][x] + 2, a[0][x] + 1)
        latestTime = max(latestTime + 2, curr)
        dync[x] = max(dync[x] + dist, latestTime)
    print(min(dync))
