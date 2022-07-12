# # from sys import stdin
# #
# # input = stdin.readline
# #
# # n = int(input())
# # #양수는 큰 수끼리, 음수는 작은수끼리, 1은 묶지 않는 것이 최대, 음수가 홀수가 되어 한개나 남는다면 0과 묶어서 지운다.
# # s = [int(input()) for _ in range(n)]
# #
# # plus = []
# # minus = []
# # zero = 0
# # one = 0
# #
# # for i in range(n):
# #     if s[i]==1:
# #         one+=1
# #     elif s[i]>0:
# #         plus.append(s[i])
# #     elif s[i]<0:
# #         minus.append(s[i])
# #     else:
# #         zero+=1
# # plus.sort(reverse=True)
# # minus.sort()
# # if len(plus)%2:
# #     plus.append(1) #편의상 (묶는거 아님)
# # if len(minus)%2:
# #     minus.append(0 if zero > 0 else 1 ) # 0은 묶어도 답에 영향가지 않으므로
# #
# # ans = one
# # for i in range(0,len(plus), 2):
# #     ans += plus[i]*plus[i+1]
# # for i in range(0, len(minus), 2):
# #     ans+= minus[i]* minus[i+1]
# #
# # print(ans)
# #
# #
# #
# #
# # for i in range(n):
# #     if s[i] == 1:
# #         one+=1
# #     elif s[i]>0:
# #         plus.append(s[i])
# #     elif s[i]<0:
# #         minus.append(s[i])
# #     else:
# #         zero+=1
# # plus.sort(reverse=True)
# # minus.sort()
# # if len(plus)%2==1: #양수의 개수가 홀수라면
# #     plus.append(1) #마지막 양수와 1을 묶어줌(값이 변하지 않으므로 편의상)
# # if len(minus)%2 ==1:
# #     if zero>0:
# #         minus.append(0) #0의 개수가 1개 이상이면 0과 묶어서 없애줌
# #     else:
# #         minus.append(1) #아니면 그냥 1과 묶어서 (값이 동일하므로) 더해줌 -> 편의상 남는 숫자없이 모두 짝지어주는 과정
# #
# # ans = one #초기값은 1의 개수만큼과 같다.
# # for i in range(0,len(plus), 2):
# #     ans+= plus[i] *plus[i+1]
# # for i in range(0, len(minus), 2):
# #     ans+= minus[i] * minus[i+1]
# #
# #
# #
# import collections
# import sys
#
# input=sys.stdin.readline
# minus=[]
# plus=[]
# one=0
# zero=0
# n= int(input())
# for _ in range(n):
#     num = int(input())
#     if num<0:
#         minus.append(-num)
#     if num>1:
#         plus.append(num)
#     if num==0:
#         zero+=1
#     if num==1:
#         one+=1
# minus= sorted(minus, key=lambda x:-x)
# plus=sorted(plus,key=lambda x:-x)
# res=0
# for i in range(0,len(plus),2):
#     if i==len(plus)-1:
#         res+= plus[i]
#     else:
#         res+=plus[i]*plus[i+1]
# for i in range(0,len(minus),2):
#     if i==len(minus)-1:
#         if zero>0:
#             zero-=1
#         else:
#             res-=minus[i]
#     else:
#         res+=minus[i]*minus[i+1]
# res+=one
# print(res)
#
#
def dfs(start,cnt):
    visit[start]=True
    for next in tree[start]:
        if visit[next]:
            continue
        else:
            cnt = dfs(next,cnt+1)
    return cnt
T= int(input())
for _ in range(T):

    n, m = map(int, input().split())
    tree = [[] for _ in range(n+1)]
    visit= [False]*(n+1)
    for _ in range(m):
        a,b = map(int, input().split())
        tree[a].append(b)
        tree[b].append(a)
    print(dfs(1,0))