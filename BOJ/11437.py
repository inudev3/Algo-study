import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
print = sys.stdout.write
n= int(input())
tree = [[] for _ in range(n+1)]
parent = [0]*(n+1)
level = [0]*(n+1)
visited = [False]*(n+1)
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def lca(a,b):
    while level[a]!=level[b]:
        if level[a]>level[b]:
            a = parent[a]
        else:
            b = parent[b]
    while a!=b:
        a = parent[a]
        b = parent[b]
    return a

def dfs(node,l):
    visited[node] =True
    level[node] = l
    for i in tree[node]:
        if not visited[i]:
            parent[i] = node
            dfs(i, l+1)
dfs(1,0) #루트노드 레벨 0
m = int(input())
for _ in range(m):
    ans = lca(*map(int, input().split()))
    print(str(ans))
    print('\n')