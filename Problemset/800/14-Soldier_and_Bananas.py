#  https://codeforces.com/problemset/problem/546/A

def bananas(k, n, w):
    total = k * ((w * (w + 1)) // 2)
    if total > n:
        return total - n
    else:
        return 0


if __name__ == '__main__':
    k, n, w = list(map(int, input().split()))
    print(bananas(k, n, w))
