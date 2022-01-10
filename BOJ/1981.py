import collections
import sys

input = sys.stdin.readline
n= int(input())
##0부터 200까지 의 수를 전부 최소값으로 하나씩 결정해보면
a = [list(map(int, input().split())) for _ in range(n)]

dx= [0,0,1,-1]
dy = [1,-1,0,0]

def bfs(mn, mx): #범위 mn, mx에서 이동가능한지 여부 체크
    if mn> a[0][0] or mx<a[0][0]:
        return False
    check = [[False] * n for _ in range(n)]
    q = collections.deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if 0<=nx<n and 0<=ny<n:
                if check[nx][ny] is False:
                    if mn<=a[nx][ny] <=mx:
                        q.append((nx,ny))
                        check[nx][ny] = True
    return check[n-1][n-1] #(n-1, n-1) 도달 여부

def go(diff): #차이에 따라 최대
    for mn in range(200-diff+1):
        if bfs(mn, mn+diff): #최대/최소 중 하나를 고정하고 나머지는 모든 경우에 수에 대하여 전부 반복
            return True
    return False

left =0
right =200
ans = 200
while left<=right:
    mid =(left+right)//2
    if go(mid):
        right = mid-1
        ans = min(ans, mid)
    else:
        left = mid+1
print(ans)


