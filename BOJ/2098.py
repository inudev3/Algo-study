n = int(input())
w = [list(map(int, input().split())) for _ in range(n)]

dp  = [[0]*(1<<(n-1)) for _ in range(n)] #시작점을 뺀다.

def solution(i,route): #i지점에서 원점으로 돌아가는데 걸리는 시간 계산
    if dp[i][route]!=0:
        return dp[i][route] ##다이나믹 프로그래밍 배열 사용
    if route== (1<<(n-1))-1: #마지막 비트(모두 방문했으면)
        if w[i][0]: #원점으로 가는 경로가 존재하면
            return w[i][0]
        else:
            return float('inf')
    min_dist = float('int')
    for j in range(1, n): #0에서 시작한다고 가정한다.
        if not w[i][j]:
            continue #경로가 없으면 건너뛰기
        if route & (1<<(j-1)):##이미 방문한 경우
            continue
        dist = w[i][j] + solution(j, route|(1<<(j-1))) #비트마스킹
        if min_dist>dist:
            min_dist = dist
    dp[i][route] = min_dist
    return min_dist

print(solution(0,0))




