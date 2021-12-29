from sys import stdin
N, M , x, y, K = map(int, stdin.readline().split())

a = [list(map(int, stdin.readline().split())) for _ in range(N)]

order = list(map(int, stdin.readline().split()))
dice  = [0] *7
ans = []
def direction(d):
    if d==1:
        return (0,1)
    elif d==2:
        return (0,-1)
    elif d==3:
        return (-1,0)
    elif d==4:
        return (1,0)
dx = [0,0,-1,1]
dy = [1,-1, 0, 0]
def changedice(d):
    if d ==1:
        dice[1], dice[3], dice[4], dice[6] = dice[4], dice[1], dice[6], dice[3]
    elif d==2:
        dice[1], dice[3], dice[4], dice[6] = dice[3], dice[6], dice[1], dice[4]
    elif d==3:
        dice[1], dice[2], dice[5], dice[6] = dice[5], dice[1], dice[6], dice[2]
    elif d==4:
        dice[1], dice[2], dice[5], dice[6] = dice[2], dice[6], dice[1], dice[5]

for k in order:
    nx, ny = x+dx[k-1], y+dy[k-1]
    if 0<=nx<N and 0<=ny<M:
        changedice(k)
        if a[nx][ny]==0:
            a[nx][ny] = dice[6]
        else:
            dice[6] = a[nx][ny]
            a[nx][ny] = 0
        x, y = nx, ny
        print(dice[1])


