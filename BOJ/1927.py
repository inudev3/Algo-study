import heapq
from sys import stdin

N= int(input())

arr = []
for i in range(N):
    eq = int(stdin.readline().rstrip())
    if eq == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
    else:
        heapq.heappush(arr, eq)

