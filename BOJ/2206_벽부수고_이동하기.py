## 빈칸에서 벽으로 이동할 수 있는건 벽을 한 번도 부순 적이 없을 때
## 따라서 정점의 정의가 달라지므로, 정점의 상태를 하나 더 만들어줘야 한다.
import collections

n,m = map(int, input().split())
board =[list(map(int,list(input()))) for _ in range(n+1)]
dist = [[[-1]*2 for _ in range(m+1)] for _ in range(n+1)]
dx =[0,0,-1,1]
dy=[1,-1,0,0]
queue=collections.deque()
queue.append((1,1,0))
dist[1][1][0] = 0
while queue:
    x,y,z = queue.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if board[nx][ny]==0 and dist[nx][ny][z]==-1:
            dist[nx][ny][z]= dist[x][y][z]+1
            queue.append((nx,ny,z))
        if z==0 and board[ny][ny]==1 and dist[nx][ny][z+1]==-1:
            dist[nx][ny][z+1] = dist[x][y][z] + 1
            queue.append((nx, ny, z+1))
if dist[n][m][0]!=-1 and dist[n][m][1]!=-1:
    print(min(dist[n][m]))
elif dist[n][m][0]!=-1:
    print(dist[n][m][0])
elif dist[n][m][1]!=-1:
    print(dist[n][m][1])
else:
    print(-1)