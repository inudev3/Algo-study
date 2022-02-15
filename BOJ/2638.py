# import collections
#
# n, m = map(int, input().split())
# dx = [0,0,1,-1]
# dy = [1,-1,0,0]
# board = [list(map(int, input().split())) for _ in range(n)]
# check = [[False] * m for _ in range(n)]
# dist = [[-1]*m for _ in range(n)]
# air = [[0]*m for _ in range(n)]
# melted = []
# def bfs():
#     q = collections.deque()
#     q.append((0,0))
#     check[0][0] = True
#     while q:
#         x, y = q.popleft()
#         for k in range(4):
#             nx, ny = x+dx[k], y+dy[k]
#             if 0<=nx<n and 0<=ny<m:
#                 if not check[nx][ny] and board[nx][ny]==0:
#                     check[nx][ny] = True
#                     board[nx][ny] =-1
#                     q.append((nx, ny))
#
# def check_melted(flag):
#     for i in range(1, n-1):
#         for j in range(1,m-1):
#             if board[i][j] == 1:
#                 cnt = 0
#                 flag = True
#                 for k in range(4):
#                     nx, ny = i+dx[k], j+dy[k]
#                     if 0<=nx<n and 0<=ny<m:
#                         if board[nx][ny] == -1:
#                             cnt+=1
#                 if cnt>=2:
#                     melted.append((i,j))
# def go_melted():
#     for node in melted:
#         x, y = node
#         board[x][y] = 0
#     for i in range(n):
#         for j in range(m):
#             if board[i][j] == -1:
#                 board[i][j] = 0
#
# while True:
#     melted = []
#     bfs()
#     check_melted()
#     go_melted()
#     break


import collections

n, m = map(int, input().split())
dx = [0,0,1,-1]
dy = [1,-1,0,0]
board = [list(map(int, input().split())) for _ in range(n)]
check = [[False] * m for _ in range(n)]
air = [[0]*m for _ in range(n)]

melted = []
ans = 0

def bfs():
    global ans
    global melted
    q = collections.deque()
    q.append((0,0))
    check[0][0] = True
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<m:
                if not check[nx][ny] and board[nx][ny]==0:
                    check[nx][ny] = True
                    q.append((nx, ny))
                elif board[nx][ny]==1:
                    air[nx][ny]+=1
                    if air[nx][ny]>=2 and not check[nx][ny]:
                        check[nx][ny] = True
                        melted.append((nx,ny))
        if not q:
            if not melted:
                break
            else:
                ans+=1
                for x,y, in melted:
                    q.append((x,y))
                    board[x][y] = 0
                melted=[]
bfs()
print(ans)

