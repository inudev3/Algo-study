# N = int(input())
# D = [0] * (N + 1)
# D[0] = 0
# D[1] = 0
# for i in range(2, N + 1):
#     D[i] = D[i - 1] + 1
#     if i % 3 == 0:
#         D[i] = min(D[i], D[i // 3] + 1)
#     if i % 2 == 0:
#         D[i] = min(D[i], D[i // 2] + 1)
#
# print(D[N])
# #
# # N, M = map(int, stdin.readline().split())
# #
# # a = list(map(int, stdin.readline().split()))
# #
# # result = 0  ##이진탐색 과정은 반복하면 시간이 지날 수록 최적화된 값이 되기 때문에 가장 마지막에 기록된 값이 정답이다.
# #
# #
# # def search(arr, target, start, end):
# #     while start <= end:
# #         res = 0
# #         mid = (start + end) // 2
# #         for i in range(N):
# #             if a[i] - mid > 0:
# #                 res += a[i] - mid
# #         if res < target:
# #             end = mid - 1  # 떡의 양이 부족
# #         else:
# #             result = mid
# #             start = mid + 1
# #
# #
# # end = max(a)
# # search(a, M, 0, end)
# # print(result)
# #
# # # 정렬된 배열에서 특정 수의 개수를 구하기
#
# N, x = map(int, stdin.readline().split())
# a = list(map(int, stdin.readline().split()))
# end = a[-1]
# start = a[0]
#
# from bisect import bisect_left, bisect_right
#
# def count_by_range(array, left, right):
#     last = bisect_right(array, right)
#     first= bisect_left(array, left)
#     return last-first
#
# count = count_by_range(a, x, x)
# print(count)
# \
# #고정점
# N = int(stdin.readline())
# a = list(map(int, stdin.readline().split()))
#
# def search(arr, target, start, end):
#     while start>=end:
#         mid = (start+end)//2
#         median = (arr[start]+arr[end])//2
#         if mid == median:




