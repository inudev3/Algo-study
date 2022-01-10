# 최소 이동 횟수 문제: BFS
import collections

dx = [-2, -2, 0, 0, 2, 2]
dy = [-1, 1, -2, 2, -1, 1]

n = int(input())

dist = [[-1] * n for _ in range(n)]
x1, y1, x2, y2 = map(int, input().split())

q = collections.deque()
q.append((x1, y1))
dist[x1][y1] = 0
while q:
    x, y = q.popleft()
    for k in range(6):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < n and 0 <= ny < n:
            if dist[nx][ny] == -1:
                dist[nx][ny] = dist[x][y] + 1
                q.append((nx, ny))

print(dist[x2][y2])
