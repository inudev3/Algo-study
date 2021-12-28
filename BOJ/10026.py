import collections
from sys import stdin
import sys

sys.setrecursionlimit(1000000)

N = int(input())


def bfsRG(start):
    q = collections.deque()
    q.append(start)
    i, j = start
    checked[i][j] = True
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < N and 0 <= ny < N:
                if not checked[nx][ny]:
                    if a[nx][ny] == a[x][y]:
                        checked[nx][ny] = True
                        q.append((nx, ny))


a = [list(map(str, stdin.readline())) for _ in range(N)]
checked = [[False] * N for _ in range(N)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
cnt = 0

for i in range(N):
    for j in range(N):
        if not checked[i][j]:
            bfsRG((i, j))
            cnt += 1
print(cnt)
cnt = 0
for i in range(N):
    for j in range(N):
        checked[i][j] = False
        if a[i][j] == 'G':
            a[i][j] = 'R'
for i in range(N):
    for j in range(N):
        if not checked[i][j]:
            bfsRG((i, j))
            cnt += 1
print(cnt)
