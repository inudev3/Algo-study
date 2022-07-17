import collections

n ,m = map(int, input().split())
dist = [-1 for _ in range(101)]
next = [i for i in range(101)]
for i in range(100):
    next[i] = i
for i in range(n+m):
    start,end = map(int, input().split())
    next[start] = end

queue = collections.deque()
queue.append(1)
dist[1] = 0
while queue:
    x = queue.popleft()
    for k in range(1,7):
       y = x+k
       if y>100: continue
       y = next[y]
       if dist[y]==-1:
           dist[y] = dist[x]+1
           queue.append(y)

## BFS 는 최소값이다.
print(dist[100])
n,m = map(int, input().split())
next = [i for i in range(101)]
dist = [-1 for _ in range(101)]
for i in range(n):
    a,b = map(int, input().split())
    next[a] = b
for i in range(m):
    a, b = map(int, input().split())
    next[a] = b

dist[1] = 0
q = collections.deque()
q.append(1)
while q:
    x = q.popleft()
    for i in range(1,7):
        y = x+i
        if y>100: continue
        y = next[y]
        if dist[y]==-1:
           dist[y] = dist[x]+1
           q.append(y)


n= int(input())
r1,c1,r2,c2 = map(int, input().split())
dx = [-2,-2,0,0,2,2]
dy = [-1,1,-2,2,-1,1]
dist = [[-1]*n for _ in range(n)]
def bfs(x,y):
    q = collections.deque()
    dist[x][y] = 0
    q.append((x,y))
    while q:
        x,y = q.popleft()
        for k in range(6):
            nx,ny = x+dx[k]+y+dy[k]
            if 0<=nx<n and 0<=ny<n and dist[nx][ny]==-1:
                dist[nx][ny] = dist[x][y]+1
                q.append((nx,ny))
bfs((r1,c1))
print(dist[r2][c2])
