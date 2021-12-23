# 토마토
from collections import deque

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

M, N = map(int, input().split())
Box = [list(map(int, input().split())) for _ in range(N)]
dist = [[-1] * M for _ in range(N)]
q = deque()
for i in range(N):
    for j in range(M):
        if Box[i][j] == 1:
            q.append((i, j))
            dist[i][j] = 0
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M:
            if Box[nx][ny] == 0 and dist[nx][ny] == -1:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] +1

ans = max([max(row) for row in dist])
for i in range(N):
    for j in range(M):
        if Box[i][j] == 0 and dist[i][j] == -1:
            ans = -1
print(ans)
