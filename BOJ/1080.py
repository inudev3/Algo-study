from sys import stdin
input = stdin.readline
n,m = map(int, input().split())
a = [list(map(int, list(input().rstrip()))) for _ in range(n)]
goal =[list(map(int, list(input().rstrip()))) for _ in range(n)]

#연산은 2번 사용할 수 없다. 2번사용하면 사용하지 않은 것과 같기 때문
#가능한 연산의 수는 (N-2)(M-2)
def flip(x,y):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            a[i][j] = 1-a[i][j]

ans = 0
for i in range(n-2):
    for j in range(m-2):
        if a[i][j] != goal[i][j]:
            ans+=1
            flip(i+1, j+1) #3x3의 맨 왼쪽 위 원소를 비교해보며 뒤집는다
for i in range(n):
    for j in range(m):
        if a[i][j] != goal[i][j]:
            print(-1)
            exit()
print(ans)
