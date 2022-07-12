# import itertools
# import sys
#
# n, m = map(int,input().split())
# field = [list(map(int, input().split())) for _ in range(n)]
#
# city=[]
# chicken=[]
# for i in range(n):
#     for j in range(n):
#         if field[i][j]==1:
#             city.append((i,j))
#         if field[i][j]==2:
#             chicken.append((i,j))
# chicken_pick = itertools.combinations(chicken, m)
# ans=10000
# for possible in chicken_pick:
#     total=0
#     for j in range(len(city)):
#         dist = 1000
#         x,y, =city[j]
#         for chickenx, chickeny in possible:
#             dist = min(dist,abs(chickenx-x)+abs(chickeny-y))
#         total+=dist
#     ans =min(ans, total)
# print(ans)
#
#
# class Solution:
#     def longestPalindrome(s: str) -> str:
#         def expand(left,right)->str:
#             while left>=0 and right<len(s) and s[left]==s[right]:
#                 left-=1
#                 right+=1
#             return s[left+1:right-1]
#
#         result=""
#         for i in range(len(s)-1):
#             result = max(result, expand(i,i), expand(i,i+1), key=len)
#         return result
#
# w,h = map(int, input().split())
# cnt = int(input())
# stores = []
# def get_distance(x,y):
#     if x==1:
#         return y
#     if x==2:
#         return w+h+w-y
#     if x==3:
#         return w+h+w+h-y
#     if x==4:
#         return w+y
# for _ in range(cnt+1):
#     x,y = map(int, input().split())
#     stores.append(get_distance(x,y))
# answer=0
# for i in range(n):
#     in_course = abs(stores[-1]-stores[i])
#     out_course = 2*(w+h)-in_course
#     answer+=min(in_course,out_course)
#
# print(answer)
import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
n,m = map(int, input().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))
start,dest = map(int, input().split())

def dfs(visited,start, limit):

    visited[start]=True
    if start==dest:
        return True
    for next,cost in graph[start]:
        if cost>=limit and not visited[next]:
            if dfs(visited,next,limit):
                return True ##갈수 있냐 없냐를 판단한다.
    return False

left=1
right=1000000000
ans=0
while left<=right:
    mid = left+ (right-left)//2
    visited = [False] * (n + 1)
    if dfs( visited,start,mid):
        if ans<mid:
            ans=mid
        left = mid+1
    else:
        right = mid-1
print(mid)
