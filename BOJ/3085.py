N = int(input())
candies = [list(input()) for _ in range(N)]
dx = [1,0]
dy = [0,1]
for i in range(N):
    for j in range(N):
        for k in range(2):
            ni, nj = i+dx[k], j+dy[k]
            if candies[i][j] == candies[ni][nj]:


def check():
    for i in range(N):
        cnt = 1
        for j in range(N):
             if a[i][j] == a[i]