# 테트로미노를 재귀로 푼다.
from sys import stdin

n, m = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
check = [[False] * m for _ in range(n)]
ans = 0


def go(x, y, sum, cnt):
    global ans
    if cnt == 4:
        if ans < sum:
            ans = sum
        return
    if not (0 < x <= n and 0 < y <= m):
        return
    if check[x][y]:
        return
    check[x][y] = True
    for k in range(4):
        go(x + dx[k], y + dy[k], sum + a[x][y], cnt + 1)
    check[x][y] = False  # 브루트포스와 DFS의 차이, 한 번 방문한 곳을 또 방문할 수 있게 해야 함


for i in range(n):
    for j in range(m):
        go(i, j, 0, 0)
        if j + 2 < m:
            temp = a[i][j] + a[i][j + 1] + a[i][j + 2]
            if i >= 1:
                temp2 = temp + a[i - 1][j + 1]
                if ans < temp2: ans = temp2
            if i < n - 1:
                temp2 = temp + a[i + 1][j + 1]
                if ans < temp2: ans = temp2
        if i + 2 < n:
            temp = a[i][j] + a[i + 1][j] + a[i + 2][j]
            if j >= 1:
                temp2 = temp + a[i + 1][j - 1]
                if ans < temp2: ans = temp2
            if j < m - 1:
                temp2 = temp + a[i + 1][j + 1]
                if ans < temp2: ans = temp2
