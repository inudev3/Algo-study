n= int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

D = [[0]*n for i in range(1,n+1)] #다 0으로 만들어야 없는 원소도 0가 합이 가능하다.
D[0][0] = tri[0][0]
for i in range(1,n):
    for j in range(i+1):
        D[i][j] = D[i-1][j]+tri[i][j] #오른쪽칸
        if j>=1 and D[i][j]< D[i-1][j-1]+tri[i][j]:
            D[i][j] = D[i-1][j-1] + tri[i][j]
print(max(D[n-1]))




