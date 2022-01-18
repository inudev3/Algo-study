
n= int(input())
a = list(map(int, input().split()))
# D = [0] * (n) #D[i]는 i번째에서 끝나는 증가하는 부분수열의 최대합.
#
# for i in range(n):
#     D[i] = a[i]
#     for j in range(i):
#         if a[i]>a[j] :
#             D[i]= max(D[j]+a[i], D[i])
# print(max(D))
# #11722
# D = [0] *(n)
# for i in range(n):
#     D[i] = 1
#     for j in range(i):
#         if a[i]<a[j]:
#             D[i] = max(D[j]+1, D[i])
#
# print(max(D))

##
D = [0] *n
for i in range(n-1, -1, -1):
    D[i] = 1
    for j in range(i+1, n):
        if a[i]>a[j]:
            D[i] = max( D[j]+1, D[i])
print(max(D))