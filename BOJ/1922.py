# from queue import PriorityQueue
# import heapq
# import sys
# input = sys.stdin.readline
# n= int(input())
# m = int(input())
# network = [[] for _ in range(n+1)]
# check = [False for _ in range(n+1)]
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     network[a].append((c,b))
#     network[a].append((c,a))
# q = []
# heapq.heappush(q, (0, 1))
# ans = 0
# while q:
#     cost, next = heapq.heappop(q)
#     if check[next]:
#         continue
#     check[next] = True
#     ans+= cost
#     for cost,next in network[next]:
#         heapq.heappush(q, (cost,next))
#
# print(ans)


# 프림알고리즘
# 정점을 한개씩 선택하는 과정으로 v-1번,
# 모든 간선 중에서 하나의 정점을 선택하는 E
# 따라서 O(VE)
# E는 V^2가 최대값이므로
# O(V^3)
# 우선 순위 큐를 사용한다면 V

import sys
input = sys.stdin.readline
n= int(input())
m = int(input())
graph = [[] for _ in range(m)]
for i in range(m):
    a,b,c = map(int ,input().split())
    graph[i].extend([c,a,b])
parent = list(range(n+1))
def Find(x):
    if parent[x]==x:
        return x
    parent[x] = Find(parent[x])
    return parent[x]
def Union(x,y):
    x = Find(x)
    y = Find(y)
    if x==y:
        return
    parent[x] = y

graph.sort(key=lambda x:x[0]) #첫번째 원소 비용을 기준으로 정렬
ans = 0
for i in range(m):
    cost, a, b = graph[i]
    x = Find(a)
    y = Find(b)
    if x!=y:
        Union(a,b)
        ans+=cost
print(ans)