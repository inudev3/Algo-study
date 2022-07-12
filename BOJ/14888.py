import sys
input = sys.stdin.readline
n= int(input())
a = list(map(int, input().split()))
ops = list(map(int, input().split()))
plus, minus, multi, div =ops
b=[]
for i in range(4):
    cnt =ops[i]
    for k in range(cnt):
        b.append(i)
def calc(a,b):
    n= len(a)
    ans = a[0]
    for i in range(1,n):
        if b[i-1]==0:
            ans+=a[i]
        if b[i-1]==1:
            ans-=a[i]
        if b[i-1]==2:
            ans*=a[i]
        if b[i-1]==3:
            ans=ans//a[i]
    return ans
res = []
def next_permutation(arr):
    n = len(arr)
    if n<2:return False
    i = n-2
    while i>=0 and arr[i]>=arr[i+1]:i-=1
    if i<0: return False
    j = i+1
    k= n-1

    while arr[i]>=arr[k]: k-=1
    arr[i],arr[k] = arr[k],arr[i]
    arr[j:] = arr[:j-1:-1]
    return arr
min=0
max=0
while True:
    ans= calc(a,b)
    if ans<min:
        min=ans
    elif ans>=max:
        max= ans
    if not next_permutation(b):
        break
print(max)
print(min)

def go(a,index, cur,plus,minus,mul,div):
    if index==n:
        return (cur,cur)
    res = []
    if plus>0:
        res.append(go(a,index+1 ,cur+a[index], plus-1, minus, mul, div))
    if minus>0:
        res.append(go(a,index+1, cur-a[index], plus, minus-1, mul,div))
    if mul>0:
        res.append(go(a,index+1, cur*a[index], plus, minus, mul-1, div))
    if div>0:
        res.append(go(a, index + 1, cur //a[index], plus, minus, mul - 1, div))
    ans = res[0]
    for p in res:
        if ans[0]<p[0]:
            ans[0] = p[0]
        if ans[1]>p[1]:
            ans[1] = p[1]
    return ans

plus,minus,div,mul = map(int, input().split())
go(a,1,a[0], plus, minus, div, mul)

n,m= map(int, input().split())
a = [list(input()) for _ in range(n)]
x1,y1,x2,y2 = -1,-1,-1,-1
for i in range(n):
    for j in range(m):
        if a[i][j]=='o':
            if x1==-1 and x2==-1:
                x1,y1 = i,j
            else:
                x2,y2 = i,j

n = int(input())
k= int(input())
sensors = list(map(int, input().split()))
right= max(sensors)
left = min(sensors)

