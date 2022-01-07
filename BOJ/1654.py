import sys
input = sys.stdin.readline
k, n = map(int, input().split())
# 길이를 결정한다.

# n개 이상을 만들 수 있으면 길이를 크게 한다.
# n개 이상을 만들 수 없으면 길이를 작게 한다.

LAN = [int(input()) for _ in range(k)]


def check(x):
    cnt = 0
    for i in range(k):
        cnt += LAN[i] // x
    return cnt >= n


ans = 0
left = 1
right = max(LAN)
while left <= right:
    mid = (left + right) // 2
    if check(mid):
        if ans < mid:
            ans = mid
        left = mid + 1
    else:
        right = mid - 1


print(ans)
