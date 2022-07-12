# import math
# n = int(input())
# costs = []
# for _ in range(n):
#     costs.append(list(map(int, input().split())))
#
# answer_bit = (1 << n)
# dp = [[-1 for _ in range(answer_bit)] for _ in range(n)]
#
# INF = 1e9
# def dfs(node, bit):
#     if bit == answer_bit:
#         if costs[node][0] == 0:
#             return INF
#         else:
#             return costs[node][0]
#     if dp[node][bit] != -1:
#         return dp[node][bit]
#     dp[node][bit] = INF
#     for i in range(n):
#         if costs[node][i] == 0 or (bit & (1 << i)):
#             continue
#         dp[node][bit] = min(dp[node][bit], costs[node][i] + dfs(i, bit | (1 << i)))
#     return dp[node][bit]
#
#
# print(dfs(0, 1))

