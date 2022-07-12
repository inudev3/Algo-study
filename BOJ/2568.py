n = int(input())

a = [-1 for _ in range(100000)]
b = [0] * n
for i in range(n):
    x, y = map(int, input().split())
    a[x] =y
    b[i] = y

d = [0]*n
v = [-1]*n
for i in range(n):
    d[i] = 1
    for j in range(i):
        if b[i] > b[j] and d[j]+1>d[i]:
            d[i] = d[j]+1
            v[i] = j

_max = max(d)
p = [i for i,x in enumerate(d) if x==_max][0] ##최대전기줄 마지막 인덱스
print(n-_max)
ans = []
def go(p):
    if p==-1:
        return
    go(v[p])
    ans.append(b[p])
go(p)


k = [i for i,x in enumerate(a) if x!=-1 and x not in ans]
print(*k)







