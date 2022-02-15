N, S = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
for i in range(1, (1 << N)):  # 공집합은 포함안하므로 0은 제외
    s = sum(a[k] for k in range(N) if (i & (1 << k)) > 0)
    if S == s:
        ans += 1



ans = 0
##s가 0일 때는 하나도 고르지 않은 부분수열이 들어가 있을 수 있으므로 1을 빼줘야 한다.
def go(index, sum):
    global ans
    if index==N:
        if sum==S:
            ans +=1
            return
    go(index+1, sum+a[index])
    go(index, sum)

go(0,0)
if S==0:
    ans -=1 #부분수열로 아무것도 고르지 않는 경우, 문제의 조건이 크기가 양수여야 하므로 빼줘야 한다. 합이 0이 아니라면 ans에 추가되지 않으므로 빼줄 필요 없음

