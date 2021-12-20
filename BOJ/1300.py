from sys import stdin

N = int(input())

k = int(input())
start, end = 1, k #k번째 인덱스에 있을 수 숫자의 최대는 k

while start <= end:
    mid = (start+end)//2
    cnt = 0
    for i in range(1, N+1):
        cnt += min(mid //i, N)
        if cnt >= k:
            ans = mid
            end = mid-1
        else:
            start = mid+1
    print(ans)


