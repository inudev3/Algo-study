from sys import stdin
import heapq

def dijkstra(start):
    q = []
    heapq.heappush(q, (start, 0))
    dist[start] = 0
    while q:
        curdist, now = heapq.heappop(q) #힙큐의 첫번째 원소는 우선순위임
        if dist[now] < curdist:
            continue
        for j in graph[now]:
            if curdist + j[1] < dist[j[0]]:
                dist[j[0]] = curdist + j[1]
                heapq.heappush(q, (dist[j[0]], j[0]))


INF = int(1e9)
V, E = list(map(int, stdin.readline().split()))
K = int(stdin.readline())
dist = [INF] * (V + 1)
graph = [[] for _ in range(V + 1)]
visited = [False] * (V + 1)
for _ in range(E):
    a, b, c = map(int, stdin.readline().split())
    graph[a].append((b, c))



dijkstra(K)
for i in range(1, V + 1):
    if dist[i] == INF:
        print("INF")
    else:
        print(dist[i])
