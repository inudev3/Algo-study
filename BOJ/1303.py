import collections

n, m = map(int, input().split())

field = [list(input()) for _ in range(m)]

visited = [[False]*n for _ in range(m)]

dx = [-1, 1, 0,0]
dy = [0,0,-1,1]
def bfs(start):
    x,y = start
    curr = field[x][y]
    visited[x][y] = True
    q = collections.deque()
    q.append(start)
    cnt=1
    while q:
        x,y = q.popleft()
        for k in range(4):
            nx,ny = x+dx[k], y+dy[k]
            if 0<=nx<m and 0<=ny<n and  field[nx][ny]==curr:
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    cnt+=1
                    q.append((nx,ny))
    return cnt
myteam = 0
enemy = 0
for i in range(m):
    for j in range(n):
        if not visited[i][j]:
            if field[i][j]=="W":
                myteam+=bfs((i,j))**2
            else:
                enemy+=bfs((i,j))**2
print(myteam, end=" ")
print(enemy, end=" ")
