import collections

N = int(input())
a = [[] for _ in range(N+1)]
for _ in range(N):
    parent, child = map(int, input().split())
    a[parent].append(child)
depth=[0] * (N+1)
check = [False] * (N+1)
parent = [0] *(N+1)
q = collections.deque()
q.append(1)
depth[1] = 0
check[1] = True
parent[1] = 0
while q:
    x = q.popleft()
    for y in a[x]:
        if not check[y]:
            q.append(y)
            check[y] = True
            parent[y] = x
            depth[y] = depth[x] +1
for i in range(1, N+1):
    print(parent[i])

#DFS
# def dfs(start):
#     stack = [start]
#     check[start] = True
#     parent[start] = True
#     depth[start] = 0
#     while stack:
#         x = stack.pop()
#         for y in a[x]:
#             if check[y] is False:
#                 stack.append(y)

