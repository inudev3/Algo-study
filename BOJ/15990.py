# import collections
#
# n = int(input())
#
# D = [[0]*3 for _ in range(100001)]
# D[1][1] = 1
# D[2][2] = 2
# D[3][3] = 3
# for i in range(1, n + 1):
#     if i>=1:
#         D[i][1] = max(D[i-1][2],D[i-1][3])
#         if i==1:
#             D[i][1] = 1
#     if i>=2:
#         D[i][2] = max(D[i-2][1], D[i-2][3])
#         if i==2:
#             D[i][2] = 2
#     if i>=3:
#         D[i][3] = max(D[i - 3][2], D[i - 3][3])
#         if i==3:
#             D[i][3] = 3
#
# ##
# D = [[0]*10 for _ in range(101)]
#
# for i in range(1,10):
#     D[1][i] = 1
# for i in range(2, n+1):
#     for j in range(10):
#             D[i][j] = 0
#             if j>=1:
#                 D[i][j] += D[i-1][j-1]
#             if j<=8:
#                 D[i][j] += D[i-1][j+1]
#
# n= int(input())
# D = [[0]*2 for _ in range(n+1)]
# D[1][1] = 1
# for i in range(1, n+1):
#     D[i][0] = D[i-1][1]+D[i-1][0]
#     D[i][1] = D[i-1][0]
#
#
# def timeconversion(s):
#     time = s.strip()
#     h, m , s = map(int, time[-2:].split(':'))
#     apm = time[-2:]


def kangaroo(x1, v1, x2, v2):
    exist = False
    while True:
        if x1 == x2:
            exist = True
            break
        if (v1 > v2 and x1 > x2) or (v1 < v2 and x1 < x2):
            break
        x1 += v1
        x2 += v2
    return 'YES' if exist else 'NO'

def calc(n,m,s):
    (m-1)+(s-1)