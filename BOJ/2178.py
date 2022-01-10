import collections
import sys
from collections import deque

input = sys.stdin.readline
n, m = map(int, input().split())
a = [list(map(int,list(input().rstrip()))) for _ in range(n)]
dist = [[0] * m for _ in range(n)]
check = [[False] * m for _ in range(n)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0, ]


q = collections.deque()
q.append((0, 0))
check[0][0] = True
dist[0][0] = 1
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k] , y + dy[k]
        if 0 <= nx < n and 0 <= ny < m:
            if check[nx][ny] is False and a[nx][ny]==1:
                check[nx][ny] = True
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(dist[n-1][m-1])