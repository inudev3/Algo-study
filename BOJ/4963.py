import collections

dx = [0, -1, -1, -1, 0, 1, 1, 1]
dy = [1, 1, 0, -1, -1, -1, 0, 1]
def bfs(a,b, cnt):
    q = collections.deque()
    q.append((a,b))
    group[a][b] = cnt
    while q:
        x, y = q.popleft()
        for i in range(8):
            nx, ny = x+dx[i], y+dy[i]
            if 0 <= nx < H and 0 <= ny < W:
                if group[nx][ny] == 0 and Map[nx][ny] == 1:
                    q.append((nx, ny))
                    group[nx][ny] = cnt


while True:
    W, H = list(map(int, input().split()))
    if W == 0 and H == 0:
        break
    Map = [list(map(int, input().split())) for _ in range(H)]
    group = [[0] * W for _ in range(H)]
    cnt = 0

    for i in range(W):
        for j in range(H):
            if Map[i][j] == 1 and group[i][j] == 0:
                cnt += 1
                bfs(i, j, cnt)
    print(cnt)
