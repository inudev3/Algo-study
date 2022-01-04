import collections
from sys import stdin

T = int(input())
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

while T:
    M, N, K = map(int, stdin.readline().split())
    farm = [[0] * 51 for _ in range(51)]
    check = [[False] * 51 for _ in range(51)]
    for _ in range(K):
        x, y = map(int, stdin.readline().split())
        farm[x][y] = 1
    q = collections.deque()
    cnt = 0
    for i in range(M):
        for j in range(N):
            if farm[i][j] == 1 and check[i][j] is False:
                q.append((i, j))
                cnt += 1
                check[i][j] = True
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx, ny = x + dx[k], y + dy[k]
                        if 0 <= nx < M and 0 <= ny < N :
                            if check[nx][ny] is False and farm[nx][ny] == 1:
                                check[nx][ny] = True
                                q.append((nx, ny))

    print(cnt)
    T -= 1
