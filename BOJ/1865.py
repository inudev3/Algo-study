
INF = 100000000

def belmanFord():
    for i in range(1, n + 1):
        for j in range(1, n+1):
            for next, cost in graph[j]:
                if dist[next] > dist[j] + cost:
                    dist[next] = dist[j] + cost
                    if i == n:
                        return False
    return True


T = int(input())

for _ in range(T):
    n,m,w = map(int, input().split())
    graph = [[] for _ in range(n+1)]
    dist = [INF] * (n+1)
    for _ in range(m):
        s, e, t = map(int, input().split())
        graph[s].append((e,t))
        graph[e].append((s,t))
    for _ in range(w):
        s,e,t = map(int, input().split())
        graph[s].append((e,-t))
    ok = belmanFord()
    print('YES' if ok else 'NO')



