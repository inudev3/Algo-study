from collections import deque
from sys import stdin
import heapq
INF = int(1e9)
dist = [INF] * (10000)

def dijsktra(S):
    global dist
    global graph
    queue = []
    heapq.heappush((0,S))
    dist[S] = 0
    while queue:
        curDist, now = heapq.heappop(queue)
        if dist[now] < curDist:
            continue
        for j in graph[now]:
            there, theredist = j[0], j[1]
            if theredist == -1:
                continue
            if curDist+theredist< dist[there]:
                dist[there] = curDist+theredist
                heapq.heappush(queue, (dist[there], there))
            #c
def bfs(start):
    global dist
    q = deque()
    q.append((0,start))
    while q:
        curDist, now = q.popleft()
        for next, nextdist in reversed[now]:
            if  dist[next] + nextdist + dist[now] == shortest
                q.append

while True:
    N, M = list(map(int, stdin.readline().split()))
    if N == 0 and M == 0:
        break
    S, D = list(map(int, stdin.readline()))
    graph = [[] for _ in range(N + 1)]
    reversed =  [[] for _ in range(N + 1)]
    for _ in range(M):
        U, V, P = map(int, stdin.readline().split())
        graph[U].append((V, P))
        reversed[V].append((U, P))
    shortest





    dijsktra()


