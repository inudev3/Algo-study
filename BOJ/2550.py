import bisect

n = int(input())
switch = list(map(int, input().split()))
idx = [0]*n
bulb = list(map(int, input().split()))
trace = []
for i in range(n):
    idx[bulb.index(switch[i])] = i ##idx[4] = 0

lis = [0]
lis[0] = idx[0]
cnt=1
for i in range(1,n):
    if idx[i]>lis[-1]:
        lis.append(idx[i])
        cnt+=1
    else:
        newIdx = bisect.bisect_left(lis, idx[i])
        lis[newIdx] = idx[i]
print(cnt)
ans=[]
for i in lis:
    ans.append(switch[i])
print(*sorted(ans))

dx = [0,0,-1,1]
dy = [-1,1,0,0]
def check(num):
    x = num//5
    y = num%5
    for k in range(4):
        nx,ny = x+dx[k], y+dy[k]
        if (0<=nx<5 and 0<=ny<5) and not visited[nx][ny]:
            next = nx*5+ny


