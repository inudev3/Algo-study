# # 순서가 바뀌면 안됨
#
# # 그룹의 합의 최대값의 최소값을 구하는 문제
# # 이분탐색으로 구할 수 있다.
# # 블루레이의 개수가 M보다 작으면 크기를 줄이고, M보다 크다면 크기를 키운다.
# # 블루레이 크기의 최소값: 레슨 한개 크기의 최대값
#
# from sys import stdin
#
# input = stdin.readline
# n, m = map(int, input().split())
#
# lessons = list(map(int, input().split()))
#
#
# def go(m, size):
#     cnt = 1
#     tmp = 0
#     for i in range(n):
#         if tmp + lessons[i] > size:
#             cnt += 1
#             tmp = lessons[i]
#         else:
#             tmp += lessons[i]
#     return cnt <= m
#
#
# def go(size):
#     cnt = 1
#     _sum = 0
#     for i in range(n):
#         if _sum + lessons[i] > size:
#             cnt += 1
#             _sum = lessons[i]
#
# left = max(lessons)
# right = sum(lessons)  # 최대크기
# ans = 0
#
# def go(size):
#     tmp=0
#     cnt=1
#     for i in range(n):
#         if lessons[i]+tmp>size:
#             cnt+=1
#             tmp = lessons[i]
#         else:
#             tmp+=lessons[i]
#         return cnt<=m
#
# left = max(lessons)
# right = sum(lessons)
#
# while left <= right:
#     mid = (left + right) // 2
#     if go(mid):
#         ans = mid
#         right = mid - 1
#     else:
#         left = mid + 1
# print(ans)
compare_num = int(input())
compare = list(map(int, input().split()))

target_num = int(input())
target = list(map(int, input().split()))


def binary_search(target):
    compare.sort()

    target_len = len(target)
    compare_len = len(compare);
    result = []

    for index in range(target_num):
        isExist = 0
        startIdx = 0
        endIdx = compare_num - 1
        while startIdx <= endIdx:
            midIdx = (startIdx + endIdx) // 2
            if target[index] == compare[midIdx]:
                isExist = 1
                break
            elif target[index] < compare[midIdx]:
                endIdx = midIdx - 1
            else:
                startIdx = midIdx + 1
        result.append(isExist)
    return result


print(*binary_search(target))
