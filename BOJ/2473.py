import sys

n = int(input())
a = sorted(list(map(int, input().split())))
_min = sys.maxsize
res = []
for i in range(n - 2):
    left, right = i +1, n-1
    while left < right:
        _sum = a[i]+a[left] + a[right]
        if _min > abs(_sum):
            _min = abs(_sum)
            res = [a[i], a[left], a[right]]
        if _sum > 0:
            right -= 1
        elif _sum < 0:
            left += 1
        else:
            print(a[i], a[left],a[right])
            sys.exit()

print(*res, sep=' ')
