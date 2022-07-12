import sys
sys.setrecursionlimit(10**9)
input =sys.stdin.readline
n,r,q = map(int, input().split())
tree = [[] for _ in range(n+1)]
visited = [False]*(n+1)
subtree= [0]*(n+1)
for _ in range(n-1):
    a,b = map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

def dfs(start):
    subtree[start] = 1
    visited[start]=True
    for next in tree[start]:
        if not visited[next]:
            dfs(next)
            subtree[start]+=subtree[next]

dfs(r)
for _ in range(q):
    print(subtree[int(input())])

n= int(input())
tree = [[] for _ in range(n+1)]
islands = {}
for i in range(n-1):
    sw, cnt, bridge = input().split()
    cnt, bridge = map(int, (cnt,bridge))
    islands[i] = (sw,cnt)
    tree[i+1].append(bridge)

def palindrome(self, s:str)->str:
    if len(s)<=1:
        return s
    i, l = 0,0
    for j in range(len(s)):
        s[j-l:j+1]==s[]


