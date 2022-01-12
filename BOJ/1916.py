import collections
import heapq
import sys

input = sys.stdin.readline
n = int(input())
m = int(input())
INF = 1e9
graph = collections.defaultdict(list)
dist = [INF] * (n + 1)
check = [False] * (n + 1)
for _ in range(m):
    u, v, cost = map(int, input().split())
    graph[u].append((v, cost))

start, end = map(int, input().split())


def dijkstra(start):
    queue = []
    heapq.heappush(queue, (0, start))
    while queue:
        curdist, now = heapq.heappop(queue)  ##최소거리부터 큐에 삽입
        if dist[now] < curdist:  # dist에 기록된 것과 비교하여
            continue
        for next, nextdist in graph[now]:
            cost = nextdist + curdist
            if dist[next] > cost:
                dist[next] = cost
                heapq.heappush(queue, (cost, next))


dijkstra(start)

print(dist[end])


