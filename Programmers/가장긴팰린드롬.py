def solution(s):
    ans=1
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        dp[i][i]=1
    for i in range(n-1):
        if s[i]==s[i+1]:
            dp[i][i+1]=1
            ans=2
    for i in range(3,n+1):
        for start in range(n-i+1):
            end = start+i-1
            if s[start]==s[end] and dp[start+1][end-1] ==1:
                dp[start][end]=1
                ans = max(ans,i)
    return ans

