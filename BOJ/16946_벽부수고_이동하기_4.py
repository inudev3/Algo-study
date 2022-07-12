import collections

n,m = map(int, input().split())
board = [list(map(int,list(input()))) for _ in range(n)]
group = [[0]*m for _ in range(n)]
checked = [[False]*m for _ in range(n)]
dx= [0,0,-1,1]
dy =[1,-1,0,0]
group_size =[]
def bfs(x,y):
    color = len(group_size)
    q = collections.deque()
    q.append((x,y))
    group[x][y] = color
    checked[x][y]=True
    cnt=1
    while q:
        a,b = q.popleft()
        for k in range(4):
            nx,ny = a+dx[k], b+dy[k]
            if 0<=nx<n and 0<=ny<m and not checked[nx][ny]:
                if board[nx][ny]==0:
                    checked[nx][ny]=True
                    group[nx][ny] = color
                    q.append((nx,ny))
                    cnt+=1
    group_size.append(cnt)

for i in range(n):
    for j in range(n):
        if board[i][j]==0 and not checked[i][j]:
            bfs(i,j)

for i in range(n):
    for j in range(m):
        if board[i][j]==0:
            print(0,end="")
        else:
            near = set()
            for k in range(4):
                nx,ny = i+dx[k], j+dy[k]
                if 0<=nx<n and 0<=ny<m:
                    if board[nx][ny]==0:
                        near.add(group[nx][ny])
            cnt=1
            for pos in near:
                cnt+=group_size[pos]
            print(cnt%10, end="")
    print()
