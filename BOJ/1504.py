# 특정한 최단경로
import heapq
from sys import stdin

MAX = 801
INF = 987654321
V, E = list(map(int, stdin.readline().split()))

graph = [[] for _ in range(V + 1)]
trace = [0] * (V + 1)

for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((c, b))
    graph[b].append((c, a))
A, B = list(map(int, stdin.readline().split()))


def dijkstra(start):
    dist = [INF] * (V + 1)
    q = []
    heapq.heappush(q, (0, start))
    dist[start] = 0
    while q:
        curdist, now = heapq.heappop(q)
        if dist[now] < curdist:
            continue
        for j in graph[now]:
            nextDist, next = j
            if curdist + nextDist < dist[next]:
                dist[next] = curdist + nextDist
                heapq.heappush(q, (nextDist, next))
    return dist


fromS = dijkstra(1)
fromA = dijkstra(A)
fromB = dijkstra(B)


path1 = fromS[A]+fromA[B]+fromB[V]
path2 = fromS[B]+fromB[A]+fromA[V]
res = min(path1, path2)
if res == INF:
    print(-1)
else:
    print(res)




