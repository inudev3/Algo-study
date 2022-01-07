import sys
input = sys.stdin.readline
sys.setrecursionlimit(100000)
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]


for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start, end = map(int, input().split())

def dfs(check, node, limit): ##설정한 중량으로 이동가능한지 검사
    if check[node]:
        return False
    check[node] = True
    if node == end:
        return True
    for next, bound in graph[node]:
        if bound>= limit and check[next] is False:
            if dfs(check, next, limit):
                return True
    return False

left = 1
Max = 1000000000
# for i in range(n):
#     bound =  max(graph[i], key=lambda x:x[1])
#     if Max < bound:
#         Max = bound
right = Max
ans=0
while left<=right:
    mid =(left+right)//2
    check = [False] * (n+1)
    if dfs(check, start,mid):
        if ans<mid:
            ans = mid
        left = mid+1
    else:
        right= mid-1
print(ans)


#중량의 최대값으로 1부터 N까지 이동할 수 있다면 중량을 늘리고
#이동할 수 없다면 중량을 줄인다.
#1부터 N까지 이동하는 것(모든 정점을 방문하는 것)은 DFS/BFS 탐색으로 수행한다.