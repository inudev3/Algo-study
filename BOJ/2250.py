# # 인오더의 순서로 열방향을 탐색할 수 있다.
# # 트리의 입력을 받을 때는 부모의 수를 카운터해서
# # 부모의 수가 0인 노드가 root가 된다. 번호 1번이 루트가 아님
# import sys
#
# sys.setrecursionlimit(10000000)
# class Node:
#     def __init__(self):
#         self.left = -1
#         self.right = -1
#         self.depth = 0
#         self.order = 0
#
#
# def inorder(node, depth):
#     global order
#     if node == -1:  ## 자식이 없는 리프 노드
#         return
#     inorder(a[node].left, depth + 1)
#     a[node].depth = depth
#     order+=1
#     a[node].order = order
#     inorder(a[node].right, depth + 1)
#
#
# order = 0
# N = int(input())
# limit = 10001
# a = [Node() for _ in range(limit)]
# cnt = [0] * limit
# posMin = [0] * limit  # 각 깊이에서 인오더 순서의 최소값과 최대값을 각각 저장
# posMax = [0] * limit
# for _ in range(N):
#     i, left, right = map(int, input().split())
#     a[i].left, a[i].right = left, right
#     if left != -1: cnt[left] += 1
#     if right != -1: cnt[right] += 1
# root = 0
# for i in range(1, N + 1):
#     if cnt[i] == 0:
#         root = i  # 부모가 없는 노드가 루트
# inorder(root, 1)
# maxDepth = 0
#
# for i in range(1, N + 1):
#     depth = a[i].depth
#     order = a[i].order
#     if posMin[depth] == 0:  # 해당깊이의 다른 노드의 순서가 정의되어 있지 않으면
#         posMin[depth] = order  # 해당노드의 순서를 최소값으로 한다.
#     else:
#         posMin[depth] = min(posMin[depth], order)
#     posMax[depth] = max(posMax[depth], order)
#     maxDepth = max(maxDepth, depth)
#
# ans = 0
# ans_level = 0
# for i in range(1, maxDepth + 1):
#     if ans < posMax[i] - posMin[i] + 1:
#         ans = posMax[i] - posMin[i] + 1
#         ans_level = i
# print(ans_level, end=" ")
# print(ans)





#
# tree = [Node() for _ in range(n+1)]
# parent = [0]*(n+1)
# Min = [0]*(n+1)
# Max = [0]*(n+1)
# for _ in range(n):
#     node, left, right = map(int, input().split())
#     tree[node].left, tree[node].right = left,right
#     if left!=-1:
#         parent[left]+=1
#     if right!=-1:
#         parent[right]+=1
# import collections
# import heapq
# import sys
# input = sys.stdin.readline
# print= sys.stdout.write
#
#
#
import itertools

sys.setrecursionlimit(1000000)


class Node:
    def __init__(self):
        self.left = -1
        self.right = -1
        self.row = 0
        self.column = 0


def inorder(node, row):
    global column
    if node == -1:
        return
    inorder(tree[node].left, row + 1)
    tree[node].row = row
    column += 1
    tree[node].column = column
    inorder(tree[node].right, row + 1)


n = int(input())
tree = [Node() for _ in range(10001)]
Min = [0] * 10001
Max = [0] * 10001
parent = [0] * 10001
column = 0

for i in range(n):
    x, b, c = map(int, sys.stdin.readline().split())
    tree[x].left = b
    tree[x].right = c
    if b != -1:
        parent[b] += 1
    if c != -1:
        parent[c] += 1

root = 0
for i in range(1, n + 1):
    if parent[i] == 0:
        root = i

inorder(root,1)
level = 0
for i in range(1,n+1):
    row = tree[i].row
    column = tree[i].column
    if Min[row]==0:
        Min[row] = column
    else:
        Min[row] = min(Min[row],column)
    Max[row] = max(Max[row], column)
    level = max(level,row)

ansMax= 0
ansLevel = 0
for i in range(1,n+1):
    if ansMax<Max[i]-Min[i]+1:
        ansMax = Max[i]-Min[i]+1
        ansLevel = i
print(str(ansLevel))
print('\n')
# print(str(ansMax))


##18352
import sys
import heapq
input = sys.stdin.readline
print=  sys.stdout.write
N,M,K,X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a,b = map(int, input().split())
    graph[a].append(b)
INF = int(1e9)
dist = [INF] *(N+1)
def dijkstra(start):
    global dist
    dist[start] = 0
    queue = []
    heapq.heappush(queue,(0,start))
    while queue:
        curDist,curr = heapq.heappop(queue)
        if dist[curr] < curDist:
            continue
        for next in graph[curr]:
            nextDist = curDist+1
            if nextDist< dist[next]:
                dist[next] = nextDist
                heapq.heappush(queue,(nextDist,next))
dijkstra(X)
ans = []
for i in range(1,N+1):
    if dist[i]==K:
        ans.append(i)
if len(ans)==0:
    print(str(-1))
else:
    for i in ans:
        print(str(i))
        print('\n')

n= int(input())
nums = list(map(int, input().split()))
s = sum(nums)
ans = 0
for n in nums:
    s = s-n
    ans+= n*s

n, m  = map(int, input().split())
nums = list(map(int, input().split()))
Sum = [0] * (n-1)
cnt = [0] *(m-1)
for i in range(n):
    if i==0:
        Sum[i] =nums[i] % m
    else:
        Sum[i] = (Sum[i-1]+nums[i]) % m
        cnt[Sum[i]]+=1
ans = cnt[0] ## 나누어떨어지는 구간
for i in range(m):
    ans+= cnt[i]*(cnt[i]-1)//2
