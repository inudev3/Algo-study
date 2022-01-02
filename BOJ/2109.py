from sys import stdin
from heapq import heappush, heappop
input = stdin.readline
n = int(input())
a=[]
for _ in range(n):
    p, d = map(int, input().split())
    a.append((p,d))
a.sort(key=lambda x: x[1], reverse=True) ## 날짜는 내림차순으로 정렬
q= []
idx = ans = 0
for i in range(10000, 0, -1):
    while idx<n and i<=a[idx][0]:
        heappush(q, -a[idx][1]) #큰 금액 힙푸쉬
        idx+=1
    if q:
        ans -= heappop(q)
print(ans)





