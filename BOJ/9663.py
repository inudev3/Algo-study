# import bisect
#
# n = int(input())
# board = [False *n for _ in range(n)]
# col=0
# row=0
# check_col = [False]*n
# check_dig = [False]*(n*2)
# check_dig2 = [False]*(n*2)
# def check(row,col):
#     if check_col[col]:
#         return False
#     if check_dig[row+col]:
#         return False
#     if check_dig2[row-col+n-1]:
#         return False
#     return True
#
# def binarySearch(left, right, target):
#     while left<right:
#         mid = (left+right)//2
#         if
#
#
#
#
#
#
# import sys
# while True:
#     n = int(input())
#     if not n:
#         break
#     price = list(map(int, input().split()))
#     dp = [0 for _ in range(n)]
#     dp[0] = price[0]
#     length = 1
#
#     for i in range(1,n):
#         start, end = 0, length-1
#         index=0
#         while start<=end:
#             mid = (start+end)//2
#             if dp[mid]<price[i]:
#                 start = mid+1
#                 index = max(index,mid+1)
#             else:
#                 end = mid-1
#         length = max(length, index+1)
#         dp[index] = price[i]
# import bisect
#
# a,b,d,n = map(int, input().split())
# dp = [0]*1000001
# for i in range(a):
#     dp[i] = 1
# for i in range(a, n+1):
#     dp[i] = (dp[i-1]+dp[i-a])%1000
#     if b<=i:
#         dp[i] = (dp[i]-dp[i-b])%1000
#
# if n>=d:
#     dp[n] = (dp[n]-dp[n-d])%1000
# print(dp[n])
#
# n= int(input())
# switch = list(map(int, input().split()))
# bulb = list(map(int, input().split()))
# switchIdx = [0] *(n+1)
# bulbIdx = [0] *(n+1)
# arr =[]
# for i in range(len(switch)):
#     switchIdx[switch[i]] = i
# for i in range(len(bulb)):
#     bulbIdx[i]  = switchIdx[bulb[i]]
#
#     if not arr or arr[-1] <bulbIdx[i]:
#         if not arr:
#         else:
#             arr.append(bulbIdx[i])
#     else:
#         idx =bisect.bisect_left(arr,bulbIdx[i])
#         arr[idx] = bulbIdx[i]
#
#
#
# n=int(input())
# k=int(input())
# sensor = sorted(list(map(int, input().split())))
# if k>=n:
#     print(0)
#     exit()
#
#
# n= int(input())
# papers = sorted([sorted(map(int, input().split())) for _ in range(n)])
# dp = [1] *n
#
# for i in range(1,n):
#     for j in range(i):
#         if papers[i][1]>=papers[j][1]:
#             dp[i] = max(dp[j]+1, dp[i])
# print(max(dp))
#
# n = int(input())
# crane = sorted(list(map(int, input().split())),reverse=True)
# m = int(input())
# box = sorted(list(map(int, input().split())),reverse=True)
#
# if box[0]>crane[0]:
#     print(-1)
#     exit()
# time=0
# while box:
#     for cr in crane:
#         for bo in box:
#             if cr>=bo:
#                 box.remove(bo)
#                 break
#     time+=1
#
# print(time)
import bisect
while True:
    try:
        n= int(input())
        prices = list(map(int, input().split()))
        dp = [prices[0]]
        cnt=1
        for i in range(1,n):

            if dp[-1]<=prices[i]:
                dp.append(prices[i])
                cnt+=1
            else:
                idx = bisect.bisect_left(dp, prices[i])
                dp[idx] = prices[i]
        print(cnt)
    except:
        break


n,m = map(int, input().split())
costs = [int(input()) for _ in range(n)]
left = min(costs)
right = sum(costs)
def check(mid):
    money = 0
    num = 0
    for cost in costs:
        if mid<cost:

while left<=right:
    mid = (left+right)//2
    now=mid
    draw=1
    for i in costs:
        if now<i:
            now=mid
            draw+=1
        now-=i
    if draw>m:
        left = mid+1
    else:
        right= mid-1


