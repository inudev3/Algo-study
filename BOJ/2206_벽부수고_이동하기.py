## 빈칸에서 벽으로 이동할 수 있는건 벽을 한 번도 부순 적이 없을 때
## 따라서 정점의 정의가 달라지므로, 정점의 상태를 하나 더 만들어줘야 한다.
import collections

n,m = map(int, input().split())
board =[[0]+list(map(int,list(input()))) for _ in range(n)]
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]
dx =[0,0,-1,1]
dy=[1,-1,0,0]
queue=collections.deque()
queue.append((0,0,0))
dist[0][0][0] = 1
while queue:
    x,y,z = queue.popleft()
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if nx<0 or nx>=n or ny<0 or ny>=m: continue
        if board[nx][ny]==0 and dist[nx][ny][z]==0:
            dist[nx][ny][z]= dist[x][y][z]+1
            queue.append((nx,ny,z))
        if z==0 and board[ny][ny]==1 and dist[nx][ny][z+1]==0:
            dist[nx][ny][z+1] = dist[x][y][z] + 1
            queue.append((nx, ny, z+1))
if dist[n-1][m-1][0]!=0 and dist[n-1][m-1][1]!=0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0]!=0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1]!=0:
    print(dist[n-1][m-1][1])
else:
    print(-1)