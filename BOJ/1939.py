import collections
import sys

n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False for _ in range(n+1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))


def bfs(start):
    visited[start] = True
    q = collections.deque()
    q.append((start,0))
    while q:
        curr, currLimit = q.popleft()
        for next, limit in graph[curr]:
            if not visited[next] or :
                visited[next]=True
                q.append(next)