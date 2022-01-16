import heapq

INF = 1e9
n, m, x = map(int, input().split())
graph = [[]*(n+1) for _ in range(2)]
for _ in range(m):
    u,v,cost = map(int, input().split())
    graph[0][u].append((cost,v))
    graph[1][v].append((cost,u))


dist = [[INF] * (n+1) for _ in range(2)]
#다익스트라: V^2, 힙을 사용하면 ElogE
def dijkstra(k): #정방향과 역방향을 구분하여 다익슼트라 시행
    dist[k][x] = 0
    q = []
    heapq.heappush((0, x))
    while q:
        curdist, now = heapq.heappop(q)
        if curdist>dist[k][now]:
            continue
        for nextdist, next in graph[k][now]:
            cost = curdist+nextdist
            if cost< dist[k][next]:
                dist[k][next] = cost
                heapq.heappush(q, (cost, next))
dijkstra(1) #정점에서 x로
dijkstra(0) #x에서 정점으로

ans = 0
for i in range(1,n+1):
    ans = max(ans, dist[1][i]+dist[0][i])
print(ans)