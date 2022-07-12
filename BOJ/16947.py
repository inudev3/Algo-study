# n= int(input())
# a= list(map(int, input().split()))
# def go(index, cnt, sum):
#
#     if cnt==3:
#         return [sum]
#     if index==n:
#         return
#     res=[]
#     res.extend(go(index+1, cnt+1, sum+a[index]))
#     res.extend(go(index+1, cnt, sum))
#
#     return res
#
# ans = go(0,0,0)
# cnt=0
# for cal in ans:
#     if 2000<=cal <=2500:
#         cnt+=1
# print(cnt)
#
T = int(input())
for _ in range(T):
    n = int(input())
    D = [[0]*2 for _ in range(41)]
    D[0][0] = 1
    D[1][1] = 1
    for i in range(2, n+1):
        D[i][0] = D[i-1][0]+ D[i-2][0]
        D[i][1] = D[i-1][1] + D[i-2][1]
    print(*D[n], sep=" ")