import collections

n,m = map(int, input().split())
board = [list(map(int, list(input()))) for _ in range(n)]
group = [[0]*m for _ in range(n)]
dx = [-1,1,0,0]
dy = [0,0,-1,1]
checked = [[False]*m for _ in range(n)]
group_size =[]
def bfsgroup(x,y):
    color = len(group_size)
    checked[x][y] = True
    q = collections.deque()
    q.append((x,y))
    group[x][y] = color
    cnt=1
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if 0<=nx<n and 0<=ny<m:
            if board[nx][ny]==0 and not checked[nx][ny]:
                checked[nx][ny] = True
                group[nx][ny] = color
                q.append((nx,ny))
                cnt+=1
    group_size.append(cnt)
cnt=0
for i in range(n):
    for j in range(m):
        if board[i][j]==0 and checked[i][j] is False:
            bfsgroup(i,j)

for i in range(n):
    for j in range(m):
        if board[i][j]==1:
            near = set()
            for k in range(4):
                ni, nj = i+dx[k], j+dy[k]
                if 0<=ni<n and 0<=nj<m:
                    if group[ni][nj]!=0 :
                        near.add(group[ni][nj])
            cnt=1
            for color in near:
                cnt+=group_size[color]
            print(cnt%10, end="")
        else:
            print(0, end="")
    print()

