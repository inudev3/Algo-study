from collections import namedtuple
from heapq import heappush, heappop
from sys import stdin
input = stdin.readline
n, k = map(int, input().split())
jewel = namedtuple('jewel', ['m', 'v', 'w'])

a = []
for _ in range(n):
    m,v = map(int, input().split())
    a.append(jewel(m,v,0)) #0은 보석, 1은 가방
for _ in range(k):
    m= int(input())
    a.append(jewel(m,0,1))
a.sort(key=lambda x: (x.m, x.w)) # 무게순으로 정렬하고 가방을 뒤쪽에
q= []
ans = 0
for p in a:
    if p.w==0: #보석이면
        heappush(q, -p.v) #가격이 큰 순서대로 푸쉬
    else: ##가방이면
        if q:
            ans-= heappop(q)# 가장 가격이 높은 보석을 pop(가방은 보석 1개씩)
print(ans)

# jewel = [map(int, input().split()) for _ in range(n)]
# bags  = [int(input()) for _ in range(k)]
# jewel.sort()
# bags.sort()
# temp = []
# ans = 0
# for bag in bags:
#     while jewel and bag>= jewel[0][0]:
#         heapq.heappush(temp, -jewel[0][1])
#         heapq.heappop(jewel)
#     if temp:
#         ans -= heapq.heappop(temp)
#     elif not jewel:
#         break


jewel =[]
bags = []
for _ in range(n):
    M, V = map(int, input().split())
    heappush(jewel, (M,-V))
for _ in range(k):
    heappush(bags, int(input()))


temp = []
ans = 0
for _ in range(k):
    bag = heappop(bags)
    while jewel and bag>= jewel[0][0]: #무게보다 작은 보석이 존재할 동안
        (m, v) = heappop(jewel) #최소 무게부터 꺼냄
        heappush(temp, -v) ##최대힙으로 무게를 넣어준다
    if temp:
        ans -= heappop(temp) #음수로 넣어줬으므로 -해주면 최대값부터 더해줌
    elif not jewel:
        break
print(ans)

