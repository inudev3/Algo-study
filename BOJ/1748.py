N = int(input())
ans = 0
start = 1
length = 1
while start <= N:
    end = start * 10 - 1
    if end > N:
        end = N
    ans += (end-start+1)*length
    start *=10
    length +=1
print(ans)


n = int(input())
ans = 0
stat = 1
length = 1
while start<=n:
    end = start*10 -1
    if end>n:
        end = n

def go(start, length, ans ):
    if start>n:
        print(ans)
        return
    end = start*10-1
    if end>n:
        end=n
    ans+= (end-start+1)* length
    length+=1
    start*=10
    go(start, length, ans)

go(1,1,0)


