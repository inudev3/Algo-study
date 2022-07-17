from sys import stdin
#백트래킹 문제
n = 9
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
check_col = [[False] * 10 for _ in range(n)] #i번째 열에 j가 있ㅇ면 True 숫자는 1부터 9까지이므로 0을 포함하여 10개
check_row = [[False]*10 for _ in range(n)] # i번째 행에 숫자 j가 있으면 True
check_square = [[False] *10 for _ in range(n)] #i번 정사각형에 숫자 j가 있으면 True i= (x//3)*3 +y/3 2
def square(i,j):
    return (i//3)*3 + j//3 #작은 정사각형의 번호를 매기는 함수
def go(z): ## 1부터 81까지
    if z== 81: #끝나면 출력
        for row in a:
            print(' '.join(map(str, row)))
        return True
    x = z//n #x행, 0부터 8까지
    y= z%n #y열
    if a[x][y]!=0: #빈칸이 아니면 다음칸
        return go(z+1)
    else:
        for i in range(1,10):
            if check_col[y][i] is False and check_row[x][i] is False and check_square[square(x,y)][i] is False:
                check_col[y][i] = check_row[x][i] = check_square[square(x,y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y] = 0
                check_col[y][i] = check_row[x][i] = check_square[square(x, y)][i] = False
    return False
for i in range(n):
    for j in range(n):
        if a[i][j] !=0:
            check_col[j][a[i][j]] = True
            check_row[i][a[i][j]] = True
            check_square[square(i,j)][a[i][j]] = True

go(0)
n = 9
a = [list(map(int, stdin.readline().split())) for _ in range(n)]
def go(z):
    if z==81:
        return True
    x=z//n
    y=z%n
    if a[x][y]!=0:
        return go(z+1)
    else:
        for i in range(1,10):
            if not check_col[y][i] and not check_row[x][i] and not check_square[square(x,y)][i]:
                check_col[y][i] = check_row[x][i] = check_square[square(x, y)][i] = True
                a[x][y] = i
                if go(z+1):
                    return True
                a[x][y]=0
                check_col[y][i] = check_row[x][i] = check_square[square(x, y)][i] = False
        return False

##재귀가 다이나믹으로 변할 수 있는 경우:
## 어떤 지점에서의 호출 그 이전 지점의 호출으로부터 독립적일 때