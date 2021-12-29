# from sys import stdin
# N= int(input())
# a = list(map(int, stdin.readline().split()))
# cnt = list(map(int, stdin.readline().split()))
# b = []
# for i, count in enumerate(cnt):
#     for _ in range(count):
#         b.append(i)
# def next_permutation(a):
#     i = len(a)-1
#     while i > 0 and a[i-1] >= a[i]:
#         i -= 1
#     if i <= 0:
#         return False
#     j = len(a)-1
#     while a[j] <= a[i-1]:
#         j -= 1
#
#     a[i-1],a[j] = a[j],a[i-1]
#
#     j = len(a)-1
#     while i < j:
#         a[i],a[j] = a[j],a[i]
#         i += 1
#         j -= 1
#
#     return True
# #+=*%
# #연산자 개수는 N-1
#
# def div(a,b):
#     if a>=0:
#         return a//b
#     else:
#         return -(-a//b)
# def calc(a,cnt):
#     n = len(a)
#     ans = a[0]
#     for i in range(1, N):
#         if b[i-1]==0: #cnt는 0부터 N-1까지 있음(인덱스 하나 작음)
#             ans += a[i]
#         elif b[i-1] == 1:
#             ans -= a[i]
#         elif b[i-1] == 2:
#             ans = ans * a[i]
#         else:
#             ans = div(ans, a[i])
#     return ans
# b.sort() #연산자를 순열을 구하는 문제
# ans=[]
# while True:
#     temp = calc(a,b)
#     ans.append(temp)
#     if not next_permutation(b):
#         break
# ans.sort()
# print(ans[-1])
# print(ans[0])


N = int(input())
a = list(map(int, input().split()))
plus, minus, mul, div = map(int, input().split())


def go(a, index, cur, plus, minus, mul, div):
    if index == len(a):
        return (cur, cur)  # 최대값, 최소값 을
    res = []
    if plus > 0:
        res.append(go(a, index + 1, cur + a[index], plus - 1, minus, mul, div))
    if minus > 0:
        res.append(go(a, index + 1, cur - a[index], plus, minus - 1, mul, div))
    if mul > 0:
        res.append(go(a, index + 1, cur * a[index], plus, minus, mul - 1, div))
    if div > 0:
        if cur >= 0:
            res.append(go(a, index + 1, cur // a[index], plus, minus, mul, div - 1))
        else:
            res.append(go(a, index + 1, (-cur // a[index]), plus, minus, mul, div - 1))

    x = max([s[0] for s in res])
    y = min([s[1] for s in res])
    return (x, y)


x, y = go(a, 1, a[0], plus, minus, mul, div)
print(x)
print(y)
