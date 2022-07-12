n, m = map(int, input().split())
board = [list(input()) for _ in range(n)]
red = (0,0)
blue = (0.0)
dest = (0,0)
for i in range(n):
    for j in range(m):
        if board[i][j]=="R":
            red = (i,j)
        if board[i][j]== "B":
            blue = (i,j)
        if board[i][j] == "0":
            dest = (0,0)
success = False
def move(dir):
    if dir=="L":
        while (board[red[0]-1][red[1]]!="#" and boardor board[red[0]-1][red[1]]!="0":
            red = (red[0]-1, red[1])

            if board[red[0]-1][red[1]]=="0":
                success= True
                return red



