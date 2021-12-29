N = int(input())

a = [[False]* N for _ in range(N)]
dx = [1,-1,-1,1]
dy = [-1,1,1,-1]
check_col = [False] * N
check_dig = [False] * (2*N-1)
check_dig2 = [False] * (2*N-1)
def check(row,col):
    if check_col[col]: #열 중복 체크
        return False
    if check_dig[row+col]: #대각선 방향
        return False
    if check_dig2[row-col+N-1]:
        return False
    return True

#행 row에 퀸의 위치를 어디에 놓을건지 계산하는 함수:

def calc(row):
    if row==N: ##끝에 도달하면 방법의 수 1개 추가
        return 1
    ans = 0
    for col in range(N): ##행에 퀸을 놓을 수 있는 모든 경우의 수 조사
        if check[row][col]:
            check_col[col] = True
            check_dig[row+col] = True
            check_dig2[row-col+N-1] = True
            a[row][col] = True
            ans+=calc(row+1)
            check_col[col] = False
            check_dig[row + col] = False
            check_dig2[row - col + N - 1] = False
            a[row][col] = False
    return ans


