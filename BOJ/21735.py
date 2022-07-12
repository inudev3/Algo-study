# n, m = map(int, input().split())
# a = list(map(int, input().split()))
#
# ans = -1
# def go(a, index, size, time):
#     global ans
#     if time > m:
#         return
#     else:
#         ans = max(ans, size)
#     if index<= len(a)-1:
#         go(a, index + 1, size+a[index+1], time + 1)
#     if index<=len(a)-2:
#         go(a, index + 2, size//2+a[index+2] , time + 1)
#
# go(a,0,1,0)
#
# print(ans)
