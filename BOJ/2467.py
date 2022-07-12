import sys

n= int(input())
a = list(map(int, input().split()))
left = 0
right = n-1
_min = sys.maxsize
l = 0
r = 0
while left<right:
    _sum = a[left]+a[right]
    if _min > abs(_sum):
        _min = abs(_sum)
        l = left
        r = right
    if _sum>0:
        right -=1
    if _sum<0:
        left +=1
    else:
        break

print(a[l], end=' ')
print(a[r])