#테트로미노를 재귀로 푼다.
from sys import stdin
N, M = map(int, stdin.readline().split())
a = [list(map(int, stdin.readline().split())) for _ in range(N)]
dx = [0,0,1,-1]
dy = [1,-1,0,0]
check = [[False] * M for _ in range(N)]
ans = 0
def go(x, y, sum, cnt):
    global ans
    if cnt==4:
        if ans<sum:
            ans = sum
        return
    if 0<x<=N and 0<y<=M:
        if not check[x][y]:
            check[x][y] = True
            for k in range(4):
                go(x+dx[k], y+dy[k], sum+a[x][y], cnt+1)
    check[x][y] = False #브루트포스와 DFS의 차이, 한 번 방문한 곳을 또 방문할 수 있게 해야 함

