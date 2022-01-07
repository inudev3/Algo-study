N, r, c = map(int, input().split())
num = 0
while N > 0:
    temp = 2 ** N // 2
    if N > 1:
        if temp > r and temp <= c:
            num += temp ** 2
            c -= temp
        elif temp <= r and temp > c:
            num += (temp ** 2) * 2
            r -= temp
        elif temp <= r and temp <= c:
            num += (temp ** 2) * 3
            r -= temp
            c -= temp
    elif N == 1:
        if r == 0 and c == 1:
            num += 1
        elif r == 1 and c == 0:
            num += 2
        elif r == 1 and c == 1:
            num += 3
    N -= 1
print(num)



# def solve(x, y, n):
#     if n == 1:
#         return 2 * x + y
#     else:
#         if x < 2 ** (n - 1):
#             if y < 2 ** (n - 1):
#                 return solve(x, y, n - 1)
#             else:
#                 return solve(x, y - 2 ** (n - 1), n-1) + 2 ** (2 * n - 2)
#         else:
#             if y < 2 ** (n - 1):
#                 return solve(x-2**(n-1), y, n-1)+ 2**(2*n-1)
#             else:
#                 return solve(x-2**(n-1), y-2**(n-1), n-1) +2**(2*n-2)*3
# n,x,y = map(int, input().split())
# print(solve(x,y,n))
