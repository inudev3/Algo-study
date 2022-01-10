
n = int(input())
a = [list(map(int, list(input()))) for _ in range(n)]
def check(x, y, size):
    for i in range(size):
        for j in range(size):
            if a[x][y] != a[x+i][y+j]:
                return False
    return True
def go(x,y, size):
    if check(x,y, size):
        print(a[x][y], end='')
        return
    m = size//2
    print('(', end='')
    for i in range(2):
        for j in range(2):
            go(x+i*m, y+j*m, m)
    print(')', end='')

go(0,0,n)