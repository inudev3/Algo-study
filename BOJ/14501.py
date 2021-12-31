##항상 경우의 수가 1억개:1초를 기준으로 그보다 적은지 많은지 판단해야 함

N = int(input())
T = list(range(N+1))
P = list(range(N+1))

for i in range(1,N+1):
    T[i], P[i] = map(int, input().split())

ans = 0
def go(day, sum ):
    global ans
    if day == N + 1:
        ans = max(ans, sum)
        return
    if day > N+1:
        return
    go(day+T[day],sum+P[day])
    go(day+1, sum)

go(1, 0)
print(ans)
D = [-1] *(N+1)
INF = int(1e9)
##DP를 활용한 재귀(메모이제이션)
#앞의 날짜의 선택에 관계없이 뒤의 날짜의 선택의 최적은 변하지 않기 때문에 다이나믹으로 풀이가능
def go(day):
    if day==N+1:
        return 0
    if day> N+1:
        return -INF #2가지 경우 값에 차이를 둬서 day==N+1에서 최대값이 될 수 있도록
    if D[day] !=-1:
        return D[day]
    t1 = go(day+1) #현재 날짜에 상담하지 않을 때
    t2 = P[day] + go(day+T[day]) #현재 날짜에 상담할 때
    D[day] = max(t1,t2)
    return D[day]
