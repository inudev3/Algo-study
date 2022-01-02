n,m, k =map(int, input().split())
cnt = 0
while n+m>=k+3 and n>=2 and m>=1:
    n-=2
    m-=1
    cnt+=1
print(cnt)