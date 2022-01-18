n, m = map(int, input().split())
a = list(map(int, input().split()))


# 구간의 개수가 m보다 작으면 최대값을 줄여주고, 구간의 개수가 m보다 크면 최대값을 증가시킨다.

def calc(a, x):
    ans = 1
    t1 = a[0]
    t2 = a[0]
    for i in range(1, n):
        if t1 > a[i]:  # 최대값
            t1 = a[i]
        if t2 < a[i]:  # 최소값
            t2 = a[i]
        if t2 - t1 > x:  # 값이 설정한 mid값보다 크면 새로운 구간을 만든다.
            ans += 1
            t1 = a[i]
            t2 = a[i]
    return ans


left = 0
right = max(a)
ans = right
while left <= right:
    mid = (left + right) // 2
    if calc(a, mid) <= m:
        right = mid - 1
        if ans > mid:
            ans = mid

    else:
        left = mid + 1
print(ans)
x