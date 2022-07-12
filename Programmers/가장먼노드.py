import collections


def solution(n, edge):
    graph = [[] for _ in range(n + 1)]
    dist = [-1 for _ in range(n + 1)]
    for e in edge:
        c, v = e
        graph[c].append(v)
        graph[v].append(c)
    q = collections.deque()
    q.append(1)
    dist[1] = 0
    maxDist = 0
    while q:
        now = q.popleft()
        for next in graph[now]:
            if dist[next] == -1:
                dist[next] = dist[now] + 1
                q.append(next)
                maxDist = max(maxDist, dist[next])
    cnt = 0
    for x in dist:
        if x == maxDist:
            cnt += 1

    return cnt