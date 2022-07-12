import collections

board = [list(input().rstrip()) for _ in range(8)]
check = [[[False]*8 for _ in range(8)] for _ in range(8)]
dx = [-1,1,0,0,-1,1,1,-1,0]
dy = [1,-1,1,-1,-1,1,0,0,0]
q = collections.deque()
q.append((7,0,0))
check[7][0][0] = True
ans=False
while q:
    x,y,t = q.popleft()
    if x==0 and y==7:ans=True
    for k in range(9):
        nx,ny = x+dx[k], y+dy[k]
        t = min(t+1,8)
        if 0<=nx<8 and 0<=ny<8:
            if nx-t>=0 and board[nx-t][ny]=="#": continue
            if

