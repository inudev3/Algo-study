# DFS 또는 BFS로 연결요소 검사를 하면 되지만 이미 연결이 행렬에 주어져 있으므로 인접리스트나 인접행렬로 만들 필요가 없다.
import heapq

N = int(input())
a = [list(map(int, input().split())) for _ in range(N)]
visited = [[0] * N for _ in range(N)]
cnt = 0  ##단지의 수


def bfs(x, y, cnt):
    queue = []
    queue.append((x, y))
    visited[x][y = 1
    while queue]:
        (a,b) = queue.pop()

for i in range(N):
    for j in range(N):
        if a[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j, ++cnt)
