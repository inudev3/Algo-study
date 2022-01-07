import sys

input = sys.stdin.readline
n, c = map(int, input().split())

# 최대값의 최소값 또는 최소값의 최대값은 대부분 이분탐색이다.

# 가장 인접한 두 공유기의 거리를 결정하여 설치 가능한 개수가 C개보다 크면 거리를 늘린다.
# 설치 가능한 개수가 C개보다 작으면 거리를 줄인다.
#  정렬 되어 있어야 한다.
lan = [int(input()) for _ in range(n)]

lan.sort()

def calc(lan, c, x):
    cnt = 1
    last = lan[0]
    for house in lan:
        if house-last >= x:
            cnt += 1
            last = house
    return cnt >= c

Max = lan[n-1]- lan[0]


left = 1
right = Max
ans = 0
while left <= right:
    mid = (left + right) // 2
    if calc(lan, c, mid):
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1

print(ans)
