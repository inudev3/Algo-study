N = int(input())
a, b = list(map(int, input()))
m = int(input())
children = [[] for _ in range(N + 1)]

cnt = 0
while m:
    x, y = list(map(int, input()))
    children[x].append(y)
    m -= 1
x = children[a] if children[a] != [] else children[b]
if x == []:
    print(-1)
while x:
    for k in x:
        if k in [a, b]:
            x = children[k]
            cnt += 1

print(cnt)
