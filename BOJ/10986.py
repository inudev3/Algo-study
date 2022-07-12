n, m = map(int, input().split())
nums = [0]+list(map(int, input().split()))

Sum = [0]*(n+1)
cnt = [0]*(n+1)

for i in range(1,n+1):
     Sum[i] = (Sum[i-1]+nums[i])%m
     cnt[Sum[i]]+=1

res = cnt[0]
for i in range(m):
    res+=cnt[i]*(cnt[i]-1)//2

print(res)
