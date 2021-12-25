# 벽을 부수는 경우는 가중치 1이고, 부수지 않는 경우는 0인문제
# 마찬가지로 큐를 2개 유지하면서 현재 큐에 가중치 0을 삽입하거나, 아니면 덱에 순서를 맞춰 삽입하는 2가지의 풀이가 있음
import collections

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

M, N = map(int, input().split())
maze = [list(map(int, list(input()))) for _ in range(N)]
limit = 101
dist = [[-1] * M for _ in range(N)]
check = [[False] * M for _ in range(N)]
q = collections.deque()
# next_queue = collections.deque()
q.append((0, 0))
dist[0][0] = 0
# while q:
#     x, y = q.popleft()
#     for i in range(4):
#         nx, ny = x + dx[i], y + dy[i]
#         if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
#             if maze[nx][ny] == 0:
#                 q.append((nx, ny))
#                 dist[nx][ny] = dist[x][y]
#             else:
#                 next_queue.append((nx, ny))
#                 dist[nx][ny] = dist[x][y] + 1
#     if not q:
#         q = next_queue
#         next_queue = collections.deque()
# print(dist[N - 1][M - 1])
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        if 0 <= nx < N and 0 <= ny < M and dist[nx][ny] == -1:
            if maze[nx][ny] == 0:
                q.appendleft((nx, ny))
                dist[nx][ny] = dist[x][y]
            else:
                q.append((nx, ny))
                dist[nx][ny] = dist[x][y] + 1
print(dist[N - 1][M - 1])
