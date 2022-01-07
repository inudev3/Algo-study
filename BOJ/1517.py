n = int(input())
arr = list(map(int, input().split()))

def solve(a, start, end):
    if start==end:
        return
    mid = (start+end)//2
    b = [0] * (end-start+1)
    ans = solve(start, mid)+solve(mid+1, end)
    i = start
    j= mid+1
    k = 0
    while i<=mid or j<=end:
        if i<=mid and (j>end or a[i]<=a[j]):
            b[k] = a[i]
            k+=1
            i+=1
        else:
            ans+= (mid-i+1) ##머지소트에서 분할된 오른쪽이 더 크면 왼쪽의 수만큼 더함
            b[k] = a[j]
            k+=1
            j+=1
    for i in range(start, end+1):
        a[i] = b[]