import collections
import sys

input = sys.stdin.readline
v = int(input())
graph = [[] for _ in range(v+1)]
for i in range(v):
    line = list(map(int, input().split()))
    for i in range(1,len(line)-1, 2):
        graph[line[0]].append((line[i], line[i+1]))

def bfs(start):
    dist = [-1] *(v+1)
    q = collections.deque()
    q.append(start)
    dist[start] = 0
    max = 0
    ans = (0,0)
    while q:
        cur = q.popleft()
        for next, distance in graph[cur]:
            if dist[next] == -1:
                dist[next] = dist[cur]+distance
                q.append(next)
                if max<dist[next]:
                    ans = dist[next], next
    return ans

dist, first= bfs(1)
secondist, second= bfs(first)

print(secondist)






