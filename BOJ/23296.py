import heapq
from collections import deque

n = int(input())
floor = [0]+list(map(int, input().split()))
indegree = [0]*(n+1)
visited = [False]*(n+1)
for i in floor:
    indegree[i] +=1
result=[]
def dfs(x):
    if visited[x]:
        return
    visited[x] = True
    result.append(floor[x])
    dfs(floor[x])

dfs(1)
elevator = []
## heap을 사용해서 indegree가 가장 작은 층부터 시작하도록 함
for i in range(1,n+1):
    if not visited[i]:
        heapq.heappush(elevator, (indegree[i],i))
while elevator:
    degree, cur = heapq.heappop(elevator)
    if visited[cur]:
        continue
    result.append(cur)
    dfs(cur)

print(len(result))
for i in result:
    print(i, end=" ")