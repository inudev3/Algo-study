import collections

n,t = map(int, input().split())
homs= set()

for _ in range(n):
    a,b =map(int, input().split())
    homs.add((a,b))


flag = False
q = collections.deque()

q.append((0,0,0))

while q:
    x,y,cnt = q.popleft()
    if y==t:
        flag = True
        break
    for i in range(-2,3):
        for j in range(-2,3):
            nx,ny = x+i,y+j
            if (nx,ny) in homs:

                    q.append((nx,ny,cnt+1))
                    homs.remove((nx,ny))


if flag:
    print(cnt)
else:
    print(-1)

