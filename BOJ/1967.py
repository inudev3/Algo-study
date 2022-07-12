import collections


class Edge:
    def __init__(self, to , cost):
        self.to = to
        self.cost = cost

def bfs(start):
    q = collections.deque()
    check[start] = True
    q.append(start)
    while q:
        x = q.popleft()
        for y in a[x]:
            if check[y.to] == False:
                dist[y.to]  = max(dist[y.to], dist[x]+y.cost)
                q.append(y.to)
                check[y.to] = True
limit = 10001

check = [False] * limit
dist = [0] *limit
N= int(input())
a = [[] for _ in range(N+1)]
for i in range(N-1):
    u,v,w = map(int, input().split())
    a[u].append(Edge(v, w))
    a[v].append(Edge(u,w))

bfs(1)
start = 1
for i in range(2, N+1):
    if dist[i] > dist[start]:
        start = i
bfs(start)
ans = dist[1]
for i in range(2, N+1):
    if ans< dist[i]:
        ans = dist[i]
print(ans)


