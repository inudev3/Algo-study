

def go(i,j): #i번째부터 j번째까지 파일을 합치는 비용
    if i==j:
        return 0
    if d[i][j]!=-1:
        return d[i][j]
    cost = sum(a[i:j+1])
    ans = d[i][j]
    for k in range(i,j):
        temp = go(i,k)+go(k+1,j)+cost
        if ans==-1 or ans>temp:
            ans=temp
    d[i][j] = ans
    return ans

T = int(input())
for _ in range(T):
    k = int(input())
    a = list(map(int, input().split()))

    d = [[-1] * k for _ in range(k)]
    print(go(0,k-1))