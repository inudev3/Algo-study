import sys


def calc(n):
    start = 1
    length = 1
    ans = 0
    while start <= n:
        end = start * 10 - 1
        if end > n:
            end = n
        ans += (end - start + 1) * length
        start *= 10
        length += 1
    return ans


n, k = map(int, input().split())
if calc(n) < k:
    print(-1)
    sys.exit(0)
left = 1
right = n
ans = 0
while left <= right:
    mid = (left + right) // 2
    length = calc(mid)
    if length < k:
        left = mid + 1
    else:
        ans = mid
        right = mid - 1
s = str(ans)
l = calc(ans)

print(s[len(s) - (l - k) - 1])
