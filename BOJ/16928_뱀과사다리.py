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


