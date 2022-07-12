import bisect

def solution(n, times):
    ans=0
    start,end= 1, max(times)*n
    while start<=end:
        mid = (start+end)//2
        curr = n
        for time in times:
            curr-= (mid//time)
        if curr>0: ##현재 주어진 시간이 부족
            start = mid+1
        else:
            end = mid-1
            ans=mid
    return ans