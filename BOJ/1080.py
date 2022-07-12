# # from sys import stdin
# # input = stdin.readline
# # n,m = map(int, input().split())
# # a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
# # goal =[list(map(int, list(input().rstrip()))) for _ in range(n)]
# #
# # #연산은 2번 사용할 수 없다. 2번사용하면 사용하지 않은 것과 같기 때문
# # #가능한 연산의 수는 (N-2)(M-2)
# # def flip(x,y):
# #     for i in range(x-1, x+2):
# #         for j in range(y-1, y+2):
# #             a[i][j] = 1-a[i][j]
# #
# # ans = 0
# # for i in range(n-2):
# #     for j in range(m-2):
# #         if a[i][j] != goal[i][j]:
# #             ans+=1
# #             flip(i+1, j+1) #3x3의 맨 왼쪽 위 원소를 비교해보며 뒤집는다
# # for i in range(n):
# #     for j in range(m):
# #         if a[i][j] != goal[i][j]:
# #             print(-1)
# #             exit()
# # print(ans)
#
# import sys
#
# n = int(input())
# a = sorted(list(map(int, input().split())))
# _min = 1e9
# res = []
#
# left, right = 0, n-1
# while left < right:
#     _sum = a[left] + a[right]
#     if _min > abs(_sum):
#         _min = abs(_sum)
#         res = [a[left], a[right]]
#     if _sum > 0:
#         right -= 1
#     elif _sum < 0:
#         left += 1
#     else:
#         print(a[left],a[right])
#         sys.exit()
#
# print(*res, sep=' ')


n, c = map(int, input().split())
weight = list(map(int, input().split()))
a = weight[:n // 2]
b = weight[n // 2:]
asum = []
bsum = []


def bruteforce(arr, _sum, index, weight):
    if index >= len(arr):
        _sum.append(weight)
        return
    bruteforce(arr, _sum, index + 1, weight)
    bruteforce(arr, _sum, index + 1, weight + arr[index])


bruteforce(a, asum, 0, 0)
bruteforce(b, bsum, 0, 0)
bsum.sort()


def upper_bound(arr, target):
    start, end = 0, len(arr)
    while start < end:
        mid = (start + end) // 2
        if arr[mid] <= target:
            start = mid + 1
        else:
            end = mid
    return end

cnt = 0
for i in asum:
    if c - i < 0: continue
    target = c - i
    cnt += upper_bound(bsum, target)
print(cnt)
