import bisect
import collections
import sys

input = sys.stdin.readline

t = int(input())
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

x = []
y = []
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum+=a[j]
        x.append(sum)
for i in range(m):
    sum=0
    for j in range(i, m):
        sum+=b[j]
        y.append(sum)

x.sort()
y.sort()
sum = 0
for num in x:
    goal = t-num
    left = bisect.bisect_left(y, goal) #lower_bound는 어떤 수 이상이 되는 가장 첫번째 인덱스
    right = bisect.bisect_right(y, goal)# upper bound는 어떤 수 초과가 되는 가장 첫번째 인덱스
    sum+=right-left ##upper_bound - lower_bound는 어떤 값의 총 개수
print(sum)

## 또는 Counter를 사용하는 방법
c = collections.Counter(y)
ans = 0
for num in x:
    ans+=c[t-num]
print(ans)
