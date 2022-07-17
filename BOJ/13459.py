LIMIT=10
def gen(k):## 4진수 생성
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] =(k&3)
        k>>=2
        ## a[i] = k%4
        ## k//4
        ## 와 같은 의미
    return a
def valid(dir):
    n= len(dir)
    for i in range(n-1):
        if dir[i]==dir[i+1]: return False ## 방향이 같으면 이동불가
        if dir[i]==0 and dir[i+1]==1: return False
        if dir[i]==1 and dir[i+1]==0:return False
        if dir[i]==2 and dir[i+1]==3: return False
        if dir[i]==3 and dir[i+1]==2: return False
    return True

def check(board,dir):
    hx=hy=rx=ry=bx=by=0
    for i in range(n):
        for j in range(m):
            if board[i][j]=='O':
                hx,hy = i,j
            elif board[i][j]=='R':
                rx,ry = i,j
            elif board[i][j]=='B':
                bx,by = i,j
    cnt = 0
    for k in dir:##dir는 벡터
        cnt+=1
        fall1=fall2 =False
        while True: ##무한루프를 도는 이유는 한 번의 이동이 두 구슬이 모두 정지할 때까지이기 때문(중간에 멈추는 경우는 고려하지 않음)
            p1 = simulate(board,k,rx,ry)
            p2 = simulate(board,k,bx,by)
            if not p1[0] and not p2[0]: ## 0번은 이동여부, 둘다 이동안하면
                break
            if p1[1]: fall1 = True
            if p2[1]: fall2=True ##한개가 구멍에 빠졌어도 이동이 계속될 수 있으므로 정지할 때까지 루프를 돈다.
        if fall2: return -1
        if fall1: return cnt
    return -1 ##아무일도 일어나지 않았다면 -1

def simulate(board,k, x,y): ##k는 방향
    if board[x][y]=='.': return (False,False) ##구슬의 위치가 빈칸이라면 종료
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    moved = False
    while True:
        nx,ny = x+dx[k], y+dy[k]
        if board[nx][ny]=='#':
            return (moved, False)
        elif board[nx][ny]=='R' or board[nx][ny]=='B':
            return (moved, False)
        elif board[nx][ny]=='.':
            board[nx][ny] = board[x][y]
            board[x][y] = '.'
            x,y = nx,ny
            moved = True
        elif board[nx][ny] == 'O':
            board[x][y] = '.'
            moved = True
            return (moved, True)
    return (False,False)
n,m = map(int, input().split())
board = [list(input()) for _ in range(n)]
ans=-1
for k in range((1<<(LIMIT*2))): ##4방향으로 움직이기 때문에 LIMIT*2 쉬프트 (4^LIMIT)
    dir= gen(k) ##4방으로 10번 움직이는 4진 비트마스크 벡터(배열)
    if not valid(dir):continue
    cur = check(board,dir)
    if cur==-1:continue
    if ans==-1 or ans>cur: ans=cur  