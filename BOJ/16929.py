# dx = [0, 0, -1, -1]
# dy = [1, -1, 0, 0]
# n, m = map(int, input().split())
# a = [input().rstrip() for _ in range(n)]
# check = [[False] * m for _ in range(n)]
#
#
# ##DFS
# def go(x, y, cnt, color): #cnt는 방문한 칸의 개수
#     if check[x][y]:
#         return (cnt - dist[x][y]) >= 4 ##방문했떤 칸은 사이클 크기가 4이상인지
#     check[x][y] = True
#     dist[x][y] = cnt
#     for k in range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if a[nx][ny] == color:
#                 if go(nx, ny, cnt + 1, color):
#                     return True
#     return False
# for i in range(n):
#     for j in range(m):
#         if check[i][j]:
#             continue
#         dist = [[0] * m for _ in range(n)] ## 시작점으로부터의 길이 초기화
#         if go(i, j , 1, a[i][j] ):
#             print('Yes')
#             exit()
# print('No')
#
#
#
# n, m = map(int, input().split())
# board = [list(map(int, input().split())) for _ in range(n)]
#
# dx = [0,0, -1,1]
# dy = [1,-1, 0,0]
# check = [[False for _ in range(m)] for _ in range(n)]
# dist =  [[0 for _ in range(m)] for _ in range(n)]
# def dfs(x,y,cnt, color):
#     if check[x][y] : return cnt-dist[x][y]>=4
#     check[x][y] = True
#     dist[x][y] = cnt
#     for k in range(4):
#         nx, ny = x+dx[k], y+dy[k]
#         if 0<=nx<n and 0<=ny<m:
#             if [nx][ny]==color:
#                 if(dfs(nx,ny,cnt+1, color)):
#                     return True
#     return False
#
# def go(x,y,px,py,color): ## 직전에 왔던 칸을 제외하고 계속방문했을 때 이전 칸을 재방문 하면 이미 4칸 이상의 사이클
#     if check[x][y]: return True
#     check[x][y] = True
#     for k in range(4):
#         nx, ny = x + dx[k], y + dy[k]
#         if 0 <= nx < n and 0 <= ny < m:
#             if (nx!=px and ny!=py) and board[nx][ny] == color:
#                 if(go(nx,ny, x,y, color)):return True
#     return False
import collections

n,m = map(int, input().split())
r,c, dir = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(n)]
checked = [[False for _ in range(m)] for _ in range(n)]



def change(dir):
    if dir==0:
        return 3
    else:
        return dir-1

def back(dir):
    if dir==0:
        return 2
    elif dir==1:
        return 3
    elif dir==2:
        return 0
    else:
        return 1
dx= [1, 0, -1, 0]
dy = [0, 1, 0, -1]
start = 0

def valid(x,y):
    for k in range(4):
        nx, ny = x+dx[k], y+dy[k]
        if not checked[x][y] or room[nx][ny]==0:
            return k
    return False


def clean(x,y,start):
    checked[x][y] = True
    nx, ny = x + dx[start], y + dy[start]
    begin = change(start)
    while begin!=start:
        if room[nx][ny]==0 or checked[nx][ny] is False:
            break
        nx, ny = x+dx[begin], y+dy[begin]
        begin  = change(begin)
    clean(nx,ny,begin)
    nx, ny = x + dx[abs(2 - start)], y + dy[abs(2 - start)]
    if room[nx][ny] == 1:
        return
    else:
        clean(nx, ny, start)



clean(r,c,dir)
cnt = 0
for i in range(n):
    for j in range(m):
        if checked[i][j]:
            cnt+=1
print(cnt)

import sys
input = sys.stdin.readline

q = collections.deque
n = int(input())
for i in range(n):
    command = input().split()
    if command[0]  == 'push':
        q.append(command[1])
    elif command[0] == 'pop':
        if not q:
            print(-1)
        else:
            print(q.popleft())
    elif command[0] == 'size':
        print(len(q))
    elif command[0] == 'empty':
        if not q:
            print(1)
        else:
            print(0)
    elif command[0] == 'front':
        if not q:
            print(-1)
        else:
            print(q[0])
    elif command[0] == 'back':
        if not q:
            print(-1)
        else:
            print(q[-1])








