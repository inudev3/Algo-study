import collections

arr = [[""]* 3072 for _ in range(6143)]

def draw(row, col):
    arr[row][col] = "*"
    arr[row+1][col-1] = '*'
    arr[row+1][col+1] = '*'

    for i in range(5):
        arr[row+2][col-2+i] = '*'

def triangle(len, row, col):
    if len==3:
        draw(row, col)
        return

    triangle(len//2, row, col)
    triangle(len//2, row+len//2, col-len//2)
    triangle(len//2, row+len//2, col+len//2)

n = int(input())
for i in range(n):
    for j in range(2*n-1):
        arr[i][j] = ' '
triangle(n, 0, n-1)#첫줄 가운데점

for i in range(n):
    for j in range(2*n-1):
        print(arr[i][j])
    print()
#모든 가중치가 1일 때 BFS 최단거리를 구하는 알고리즘은 BFS
#1이 아니라면 다익스트라가 최단거리 알고리즘
##정점과 간선의 개수가 시간제한을 초과하지 않아야함
#O(V+E)가 1억개 이상이 되면 시간 초과가능성이 생긴다.(점점+간선 개수)
#할 수 있는 게 같지 않으면 같은 정점이 아니다. 따라서 이동할 수 있는 방법이 달라지면 두정점은 다른 정점이다.


s = int(input())
dx = []
dist = [-1] * (s+1)
board =[]
q = collections.deque()
q.append(1)
dist[1] = 0
while q:
    x = q.popleft()
    if board:
        for nxt in [x-1, x+board.pop()]:
            if dist[nxt] !=-1 and 0<=nxt<=2000:
                dist[nxt] = dist[x]+1
                q.append(nxt)
    else:
        board.append(x)
        dist[x]+=1

