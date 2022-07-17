import sys
import heapq
import math
n,m,k = map(int, input().split())
graph = [[] for _ in range(n+1)]

input = sys.stdin.readline
dist = [[math.inf for _ in range(k + 1)] for _ in range(n + 1)]
for _ in range(n):
    a,b,time= map(int, input().split())
    graph[a].append((b,time))
    graph[b].append((a,time))


def dijkstra(start):
    global dist
    cnt=0
    queue = []
    dist[start][cnt]=0
    heapq.heappush(queue, (0,start,cnt))
    while queue:
        total,x,cnt = heapq.heappop(queue)
        if dist[x][cnt]<total:
            continue
        for next, time in graph[x]:
            next_dist=time+total

            if dist[next][cnt]> next_dist:
                dist[next][cnt] = next_dist
                heapq.heappush(queue, (next_dist, next, cnt))
            if cnt<k and dist[next][cnt+1]>total:
                dist[next][cnt+1] = total
                heapq.heappush(queue, (total, next, cnt+1))

dijkstra(1)
print(min(dist[n]))

n = int(input())
LIMIT = 5
def gen(k): ##4진수 5자리
    a = [0]*LIMIT
    for i in range(LIMIT):
        a[i] = (k&3)
        k >>= 2
    return a
board = [list(map(int, input().split())) for _ in range(n)]
def check(a, dirs):
    n= len(a)
    d = [row[:] for row in a]
    for dir in dirs:
        ok=False
        merged = [[False]*n for _ in range(n)]
    while True:
        ok=False



