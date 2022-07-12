# # n, m, k = map(int, input().split())
# # nums = []
# # for _ in range(n):
# #     nums.append(int(input().rstrip()))
# # tree = [0] * (len(nums) * 4)
# #
# #
# # def init(start, end, index):
# #     if start == end:
# #         tree[index] = nums[start]
# #         return tree[index]
# #     mid = (start + end) // 2
# #     # 좌측 노드와 우측 노드를 채워주면서 부모 노드의 값도 채워준다.
# #     tree[index] = init(start, mid, index * 2) + init(mid + 1, end, index * 2 + 1)
# #     return tree[index]
# #
# #
# # def interval_sum(start, end, index, left, right):
# #     if left > end or right < start:
# #         return 0
# #     if left <= start and right >= end:
# #         return tree[index]
# #     mid = (start + end) // 2
# #     return interval_sum(start, mid, index * 2, left, right) + interval_sum(mid + 1, end, index * 2 + 1, left, right)
# #
# #
# # def update(start, end, index, goal, value):
# #     if goal < start or goal > end:
# #         return
# #     tree[index] += value
# #     if start == end:
# #         return
# #     mid = (start + end) // 2
# #     update(start, mid, index * 2, goal, value)
# #     update(mid + 1,end, index * 2 + 1, goal, value)
# #
# # init(0,len(nums)-1, 1)
# # print()
# # for _ in range(m+k):
# #     command, a, b = map(int, input().split())
# #
# #     if command==1:
# #         a -=1
# #         nums[a] = b
# #         update(0,len(nums)-1,1, a, b-nums[a])
# #     else:
# #         print(interval_sum(0,len(nums)-1,1, a-1,b-1))
# #
# from collections import defaultdict
#
# result = defaultdict(0)
#
#
# def check(A ,B):
#     cnt=0
#     for i in range(len(A)):
#         if A[i]!=B[i]:
#             cnt+=1
#     return cnt==1
# def dfs(connected, checked, start, target, cnt):
#     if start==target:
#         return cnt
#     checked[start] = True
#     for next in range(len(connected[start])):
#         if connected[start][next] and checked[next] is False:
#             checked[next] = True
#             cnt+=1
#             dfs(connected, checked, next, target, cnt)
#
# def solution(begin, target, words):
#     words.extends([begin])
#     if target not in words:
#         return 0
#     connected = [[False for _ in range(len(words))] for _ in range(len(words))]
#     checked = [False for _ in range(len(words))]
#     dist = [0 for _ in range(len(words))]
#     for i in range(len(words)):
#         for j in range(i+1, len(words)):
#             connected[i][j] = check(words[i],words[j])
#     ans = dfs(connected,checked, 0, words.index(target), 0)
#     return ans
#
# # print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))
# words =["hit"].extend(["hot", "dot", "dog", "lot", "log", "cog"])
# print(words)
#

# from collections import defaultdict, Counter
#
# def solution(participant, completion):
#     result = defaultdict(int)
#     ans = []
#     for player in participant:
#         result[player] += 1
#     for player in completion:
#         result[player] -= 1
#     for item in result.items():
#         if item[1] > 0:
#             for i in range(item[1]):
#                 ans.append(item[0])
#     return ans
#
#
# print(solution(["leo", "kiki", "eden"],	["eden", "kiki"]))
#

from collections import defaultdict, Counter
def solution(genres, plays):
    hash=defaultdict(list)
    songs  = list(zip(genres, plays))
    res =[]
    ans=[]
    for i in range(len(songs)):
        genre, play = songs[i]
        hash[genre].append((play,i))
    for genre in hash:
        hash[genre] = sorted(hash[genre], key=lambda x:x[0], reverse=True)
        res.append((sum(hash[genre][0]), hash[genre]))
        res = sorted(res, key=lambda x:x[0], reverse=True)
        total, rest = zip(*res)
        plays, indexes = zip(*rest)
        ans.extend(indexes)
    return ans

print(solution(["classic", "pop", "classic", "classic", "pop"],	[500, 600, 150, 800, 2500]))