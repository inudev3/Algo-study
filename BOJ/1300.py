from sys import stdin

n, k = map(int, input().split()) #k는 순서

left = 1
right = n*n #전체 수의 개수
ans = 0
while left<=right:
    mid = (left+right)//2
    cnt=0
    for i in range(1, n+1):
        cnt+= min(n, mid//i) #작거나 같은 수의 개수를 포함
    if cnt>=k:
        ans=mid
        right =mid-1
    else:
        left= mid+1
print(ans)

