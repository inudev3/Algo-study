n= int(input())

tri = [list(map(int, input().split())) for _ in range(n)]

D = [[0]*i for i in range(1,n+1)]
D[2] = tri[0]
