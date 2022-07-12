

n = int(input())
lines = []
for i in range(n):
    x, y = map(int, input().split())
    lines.append((x, y))

lines.sort(key=lambda x:x[0])
start = end = -1e9
dist = 0

for line in lines:
    if line[0]<=end:
        end = max(line[1], end)
    if line[1]<=end:
        continue
    elif line[1]>end:
        if line[0]>end:
            dist+= line[1]-line[0]
            start = line[0]
            end = line[1]
        else:
            dist+=line[1]-end
            end=line[1]
print(dist)
