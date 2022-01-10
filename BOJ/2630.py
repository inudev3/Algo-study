import sys

input = sys.stdin.readline
n = int(input())

a = [list(map(int, input().split())) for _ in range(n)]
def same(x,y,size):
    for i in range(size):
        for j in range(size):
            if a[x][y] != a[x+i][y+j]:
                return False
    return True
cnt= [0]* 2
def go(x,y,size):
    if same(x,y,size):
        cnt[a[x][y]]+=1
        return
    m = size//2
    for i in range(2):
        for j in range(2):
            go(x+i*m, y+j*m, m)

go(0,0,n)
for i in range(2):
    print(cnt[i])
