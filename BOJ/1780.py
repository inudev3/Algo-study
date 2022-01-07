from collections import defaultdict
from sys import stdin

n = int(stdin.readline())

a = [list(map(int, stdin.readline().split())) for _ in range(n)]


def same(x, y, n):
    for i in range(n):
        for j in range(n):
            if a[x + i][y + j] != a[x][y]:
                return False
    return True


cnt = [0] * 3


def solve(x, y, n):
    if same(x, y, n):
        cnt[a[x][y] + 1] += 1  # (x,y)칸에 있는 숫자의 개수를 1 증가(-1,0,1)이므로 편의상 0,1,2로 바꿔줌
        return
    m = n // 3
    for i in range(3):
        for j in range(3):
            solve(x + i * m, y + j * m, m)


solve(0, 0, n)
for i in range(len(cnt)):
    print(cnt[i])

