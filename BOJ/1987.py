import collections
from sys import stdin

r, c = map(int, input().split())
check = [False] * 26
board = [list(input().rstrip()) for _ in range(r)]
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]
dist = [[-1] * c for _ in range(r)]
q = collections.deque()
dist[0][0] = 1
q.append((0, 0))
while q:
    x, y = q.popleft()
    for k in range(4):
        nx, ny = x + dx[k], y + dy[k]
        if 0 <= nx < r and 0 <= ny < c:
            ch = ord(board[ny][ny]) - ord('A')
            if check[ch]:
                continue
            check[ch] = True
            dist[nx][ny] = dist[x][y] + 1
            q.append((nx, ny))
ans = 0
for i in range(r):
    for j in range(c):
        if dist[i][j] == -1:
            continue
        if ans < dist[i][j]:
            ans = dist[i][j]
print(ans)
