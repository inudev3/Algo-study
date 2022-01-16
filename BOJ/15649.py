# # M, N = list(map(int, input()))
# #
# # check = [False] * 10
# # a = [0] * 10
# # #순서가 중요함
# # #재귀함수의 경우
# #
# # def go(index, n, m): ##index번째의 수를 결정한다.
# #     if index==m:
# #         print(a) ##재귀함수는 종료조건이 중요하다.
# #     for i in range(1, n+1):
# #         if check[i]:
# #             continue
# #         check[i]= True
# #         a[index] = i ##함수의 호출전에 변경을 끝내야 한다.
# #         go(index+1, n, m)
# #         check[i] = False ##함수의 호출이 끝났으면 경우가 끝났으므로 다시 상태를 돌려야 한다.
# # go(0, N, M)
# #
# #
# # ##15650
# #
# # def go(index, start,  n, m):#재귀함수는 변화를 기록하는 것이 중요하다.
# #     if index ==m:
# #         print(a)
# #     for i in range(start, n+1):
# #         a[index] =i
# #         go(index+1, i+1, n, m)
# #
# # def go(index, selected, n, m): ##순서가 아니라 매 숫자마다 선택하는문제로 재귀함수 풀이, selected가 기존의 index
# #     if selected ==m:
# #         print(a)
# #     if index>n: return
# #     a[selected] = index
# #     go(index+1, selected+1, n ,m)
# #     a[selected] = 0
# #     go(index+1, selected, n, m)
# #
# # #15651
# # #중복선택 가능
# #
# # def go(index, n, m):
# #     if index==m:
# #         print(a)
# #     for i in range(1, n+1):
# #         a[index] = i ##함수의 호출전에 변경을 끝내야 한다.
# #         go(index+1, n, m)
# #
# # #15652
# # #중복가능, 비 내림차순
# #
# # def go(index, start, n, m):
# #     if index==m:
# #         print(a)
# #     for i in range(start, n+1):
# #         a[index] = i #정답배열
# #         go(index+1, i, n, m)
# # def go(index, selected, n, m):
# #     if selected==m:
# #         print(a)
# #     if index>n:
# #         return
# #     for i in range(m-selected, 0, -1):
# #         cnt[index] = i ## 횟수가 몇번 반복되는지 기록
# #         go(index+1, selected+i, n, m)
# #
# # #다이나믹_: 점화식을 정의한다.
# # # 문제를 작게 만들수 있는 방법이 주어졌다면 이용하고, 없다면 찾는다.
# # n, m = map(int, input().split())
# # check = [False] * (n+1)
# # a= [0]*(n+1)
# # def go(index, n, m, ans):
# #     if index==m:
# #         for x in ans:
# #             if x !=0:
# #                 print(x)
# #         return
# #     for i in range(1, n+1):
# #         if not check[i]/:
# #             check[i] = True
# #             a[index] = i
# #             go(index+1, n, m )
# #             check[i] = False
# # go(0, n, m)
#
#
# # #15650
# import sys
#
# n, m = map(int, input().split())
# a = [0] * m
#
#
# # def go(index, start, n, m):
# #     if index==m:
# #         for x in a:
# #             if x!=0:
# #                 print(x, end=" ")
# #         return
# #     for i in range(start, n+1):
# #         a[index] = i
# #         go(index+1, i+1, n, m)
# #
# # go(0,1,n, m)
#
#
# ##선택 유형
# def go(index, selected, n, m):
#     if selected == m:
#         sys.stdout.write(' '.join(map(str, a)) + '\n')
#         return
#     if index > n:
#         return
#     a[selected] = index
#     go(index + 1, selected + 1, n, m)
#     a[selected] = 0
#     go(index + 1, selected, n, m)
#
#
# go(1, 0, n, m)
#
# #15651
# def go(index, n, m):
#     if index==m:
#         print(a)
#         return
#     for i in range(1, n+1):
#         a[index] = i
#         go(index+1, n, m)
#
# #15652
# def go(index, start, n, m):
#     if index==m:
#         print(' '.join(map(str,a)))
#         return
#     for i in range(start, n+1):
#         a[index] = i
#         go(index+1, i, n, m)
# go(0,n,m)
#
# a =[0]*m
# cnt = [0]*m
# #선택유형
# def go(index, selected, n, m):
#     if selected==m:
#         print(' '.join(map(str, a)))
#         return
#     if index>n:
#         return
#     for i in range(m-selected, 0, -1):
#         cnt[index] = i
#         go(index+1, selected+i, n, m)
#     cnt[index] = 0
#     go(index+1, selected, n, m)

T = int(input())
mod = 1000000009
D = [0] * 1000001
D[0]=1
for i in range(1000001):
    if i >= 1:
        D[i] += D[i - 1]
    if i >= 2:
        D[i] += D[i - 2]
    if i >= 3:
        D[i] += D[i - 3]
    D[i] %= mod
for _ in range(T):
    n = int(input())
    print(D[n])