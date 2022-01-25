import heapq

INF = 1e9
n, m, x = map(int, input().split())
graph = [[] for _ in range (n + 1)]
graph_r = [[] for _ in range(n+1)]
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((cost, v))
    graph_r[v].append((cost, u))

dist = [INF] * (n + 1)
dist_r =  [INF] * (n + 1)

# 다익스트라: V^2, 힙을 사용하면 ElogE

def dijkstra(dist, graph):  # 정방향과 역방향을 구분하여 다익슼트라 시행
    dist[x] = 0
    q = []
    heapq.heappush(q,(0, x))
    while q:
        curdist, now = heapq.heappop(q)
        if curdist > dist[now]:
            continue
        for nextdist, next in graph[now]:
            cost = curdist + nextdist
            if cost < dist[next]:
                dist[next] = cost
                heapq.heappush(q, (cost, next))

# 단방향
# x로 가는 다익스트라
# x에서 오는 다익스트라


dijkstra( dist, graph)  # 정점에서 x로
dijkstra(dist_r, graph_r)  # x에서 정점으로

ans = 0
for i in range(1, n + 1):
    ans = max(ans, dist[i]+dist_r[i])
print(ans)

