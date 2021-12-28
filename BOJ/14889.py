# N = int(input())
# S = [list(map(int, input().split())) for _ in range(N)]
# first = []
# second = []
#
#
# def go(index, first, second): #각 사람이 어떤 팀에 들어갈 것인지 결정(매번 인덱스마다) 2^N
#     if index == N:
#         if len(first) != N // 2:
#             return -1
#         if len(second) != N // 2:
#             return -1
#         t1 = 0
#         t2 = 0
#         for i in range(N // 2):
#             for j in range(N // 2):
#                 t1 += S[first[i]][first[j]]
#                 t2 += S[second[i]][second[j]]
#         diff = abs(t1 - t2)
#         return diff
#     if len(first) > N // 2:
#         return -1
#     if len(second) > N // 2:
#         return -1
#     ans = -1
#     t1 = go(index + 1, first + [index], second)
#     if ans == -1 or (t1 != -1 and ans > t1):
#         ans = t1
#     t2 = go(index + 1, first, second + [index])
#     if ans == -1 or (t2 != -1 and ans > t2):
#         ans = t2
#     return ans
# ##브루트포스에서 경우의수를 만들어 불가능한 경우를 제외하는 것이 백트래킹
#
# #비트마스크
# ans = -1
# for i in range(1<<N):
#     for j in range(N):
#         if i&(1<<j): #번호 j가 첫번째 팀에 포함되는 경우의 수
#             first.append(j)
#         else:
#             second.append(j)
#     if len(first) != N//2:
#         continue
#     t1 = 0
#     t2=0
#     for l1 in range(N//2):
#         for l2 in range(N//2):
#             t1 += S[first[l1]][first[l2]]
#             t2 += S[second[l1]][second[l2]]
#     diff = abs(t1-t2)
#     if ans==-1 or ans>diff:
#         ans = diff
# print(ans)


from sys import stdin

def next_permutation(a):
    i = len(a)-1
    while i>0 and a[i]<=a[i-1]:
        i-=1
    if i<0:
        return False
    j = len(a)-1
    while a[j]<=a[i-1]:
        j-=1
    a[i-1], a[j] = a[j] ,a[i-1]
    j = len(a)-1
    while i>j:
        a[i], a[j] = a[j], a[i]
        i+=1
        j-=1
    return True
N = int(input())
S = [list(map(int, stdin.readline().split())) for _ in range(N)]
b = [0] *N
for i in range(N//2):
    b[i] = 1
b.sort()

ans = 3214287655
while True:
    first = []
    second = []
    for i in range(N):
        if b[i]==1:
            second.append(i)
        else:
            first.append(i)
    one=0
    two = 0
    for i in range(N // 2):
        for j in range(N // 2):
            if i == j:
                continue
            one += S[first[i]][first[j]]
            two += S[second[i]][second[j]]
    diff = abs(one-two)
    if ans>diff:
        ans= diff
    if not next_permutation(b):
        break
print(ans)




