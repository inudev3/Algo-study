from collections import namedtuple

T = int(input())
Edge = namedtuple('Edge', ['from', 'to', 'cost'])
def belmanFord(start):
    dist[start] = 0
    for i in range(n + 1):
        for j in range(1, n + 1):
            for next, cost in graph[j]:
                if dist[next] > dist[j] + cost:
                    dist[next] = dist[j] + cost
                    if i == n:
                        return False
    return True

for _ in range(T):
    n, m, w = map(int, input().split())
    graph = [] *(n+1)
    wormhole = [] *(n+1)
    dist = [10001] * (m)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(w):
        s,e,t = map(int, input().split())
        wormhole[s].append((e,t))
    print('YES' if belmanFord(1) else 'NO')



