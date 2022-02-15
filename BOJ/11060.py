n = int(input())

a = [0]+list(map(int, input().split()))
D = [-1]*(n+1)
for i in range(1, n):
     for j in range(i):
         if i-j<= a[j] and D[j]!=-1:
             if D[i] == -1 or D[i]>D[j]+1:
                 D[i] = D[j]+1
print(D[n-1])

##방법 2 어디로 갈 수 있는가

D[0] = 0
for i in range(n-1):
    if D[i] == -1:
        continue
    for j in range(1, a[i]+1):
        if i+j>=n:
            break
        if D[i+j] == -1 or D[i+j]>D[i]+1:
            D[i+j] = D[i]+1
