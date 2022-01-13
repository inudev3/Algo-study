n = int(input())
d = [0] *(n+1)
d[0] = 0
d[1] = [1]
for i in range(2, n+1):
    d[n] =d[n-1]+ d[n-2]
INF = 1000000007
print(d[n]%INF)
