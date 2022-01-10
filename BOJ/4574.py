import sys
input = sys.stdin.readline

def convert(s):
    return (ord(s[0])-ord('A'), ord(s[1])-ord('1'))
def square(x,y):
    return (x//3)*3 + (y//3)
def can(x,y,num):
    return not c[x][num] and not c2[y][num] and not c3[square(x,y)][num]

def check(x,y,num, what:bool):
    c[x][num] = what #행, 열에 체크
    c2[y][num] = what
    c3[square(x,y)][num] = what # 작은 정사각형에 체크

def check_range(x,y):
    return 0<=x<n and 0<=y<n

def go(z):
    if z==81:
        for i in range(n):
            print(''.join(map(str, a[i])))
        return True
    x= z//n
    y = z%n
    if a[x][y]!=0:
        return go(z+1)
    else:
        for k in range(2):
            nx, ny = x+dx[k], y+dy[k]
            if not check_range(nx,ny) or a[nx][ny]!=0:
                continue
            for i in range(1,10):
                for j in range(1,10): ##도미노는 순서를 구분하지 않지만 스도쿠 보드에서는 구분하므로 전부 해봐야 함
                    if i==j or domino[i][j]: #숫자는 달라야함
                        continue
                    if can(x,y,i) and can(nx,ny, j):
                        check(x,y,i,True)
                        check(nx,ny,j,True)
                        domino[i][j] = domino[j][i] = True
                        a[x][y] = i
                        a[nx][ny] = j
                        if go(z+1):
                            return True
                        check(x,y,i,False)
                        check(nx,ny,j,False)
                        domino[i][j] = domino[j][i] = False
                        a[x][y] = 0
                        a[nx][ny] = 0
        return False



n=9
dx = [0,1]
dy = [1,0]
tc = 1
while True:
    c = [[False]*10 for _ in range(10)]
    c2 = [[False]*10 for _ in range(10)]
    c3 = [[False]*10 for _ in range(10)]
    domino = [[False]*10 for _ in range(10)]
    a = [[0]*9 for _ in range(n)]
    m = int(input())
    if m ==0:
        break
    for _ in range(m):
        n1, s1, n2, s2 = input().split()
        n1 = int(n1)
        n2 = int(n2)
        x1, y1 =convert(s1)
        x2,y2 = convert(s2)
        a[x1][y1] = n1
        a[x2][y2] = n2
        domino[n1][n2] = domino[n2][n1] = True
        check(x1,y1,n1, True)
        check(x2,y2,n2, True)
    temp = input().split()
    for i in range(1,10):
        s = temp[i-1]
        x,y, = convert(s)
        a[x][y]= i
        check(x,y,i, True)
    print("Puzzle %d" %tc)
    go(0)
    tc+=1