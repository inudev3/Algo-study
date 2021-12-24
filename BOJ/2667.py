# DFS 또는 BFS로 연결요소 검사를 하면 되지만 이미 연결이 행렬에 주어져 있으므로 인접리스트나 인접행렬로 만들 필요가 없다.
import heapq
from collections import deque

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
group = [[0] * N for _ in range(N)]
cnt = 0  ##단지의 수
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def bfs(x, y, cnt):
    q = deque()
    q.append((x, y))
    group[x][y] = cnt
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if 0 <= nx < N and 0 <= dy < N:
                if a[nx][ny] == 1 and group[nx][ny] == 0:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


for i in range(N):
    for j in range(N):
        if a[i][j] == 1 and group[i][j] == 0:
            cnt+=1
            bfs(i, j, cnt)
