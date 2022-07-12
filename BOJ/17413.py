# import heapq
#
# S = input()
#
# tag = False
# stack = []
#
# for char in S:
#     if char=="<":
#         while stack:
#             print(stack.pop())
#         tag = True
#         print(char)
#     elif char ==">":
#         tag= False
#         print(char)
#     elif tag is True:
#         print(char)
#     else:
#         if char== " ":
#             while stack:
#                 print(stack.pop())
#                 print(char)
#         else:
#             stack.append(char)
# while stack:
#     print(stack.pop())
# print()

n, p = map(int ,input().split())
data = [[] for _ in range(7)]
ans=0
for _ in range(n):
    num,melody = map(int, input().split())
    if data[num] and data[num][-1]==melody:
        continue
    while data[num] and data[num][-1]>melody:
        data[num].pop()
        ans+=1
    if data[num] and data[num][-1]==melody:
        continue
    data[num].append(melody)
    ans+=1

print(ans)


import heapq
n= int(input())
q = []
for i in range(n):
    heapq.heappush(q, int(input()))
    heapq.heapify(q)
    print(q[i//2 if (i+1)%2 else i//2-1])
