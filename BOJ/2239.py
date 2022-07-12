import sys
from sys import stdin
input = stdin.readline

board = [list(map(int, input().split())) for _ in range(9)]
zeros = [(i,j) for i in range(9) for j in range(9) if not board[i][j]]
for r in range(9):
    for c in range(9):
        if board[r][c] ==0:
            zeros.append((r,c))

def rowCheck(r, num):
    for c in range(9):
        if board[r][c] == num:
            return False
    return True
def colCheck(c, num):
    for r in range(9):
        if board[r][c] == num:
            return False
    return True

def squareCheck(r,c,num):
    nr = (r//3)*3
    nc = (c//3)*3
    for i in range(3):
        for j in range(3):
            if board[nr+i][nc+j] == num:
                return False
    return True
cand = []
def bt(n):
    if n == len(zeros):
        for i in board:
            print(*i, sep='')
        sys.exit()
    x,y = zeros[n]
    a,b = x//3, y//3

    for i in range(10):
        if squareCheck(x,y, i) and colCheck(y,i) and rowCheck(x,i):
            cand.append(i)
    for i in cand:
        board[x][y] = i
        bt(n+1)

n = int(input())
dp = [[0 for _ in range(2)] for _ in range(n+1)]
dp[1][1] = 1
for i in range(2, n+1):
    dp[i][0] = dp[i-1][0]+dp[i-1][1]
    dp[i][1] = dp[i-1][0]

D = [1 for _ in range(n)]
a = list(map(int, input().split()))
v = [-1]*n
for i in range(1, n+1):
    for j in range(i+1, n+1):
      if a[j]>a[i] and D[i]+1>D[j]:
          D[j] = D[i]+1
          v[j] = i

def go(p):
    if p==-1:
        return
    go(v[p])
    print(a[p])

p = [i for i,x in enumerate(D) if x == max(D)][0]
print(max(D))
def go(p):
    if p==-1:
        return
    go(v[p])
    print(a[p], end=' ')

while p==-1:
    print(a[p], end=' ')
    p = v[p]