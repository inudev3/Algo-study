from collections import namedtuple
from sys import stdin
#빨리 끝나는 것부터 배정한다.
input = stdin.readline
Meeting = namedtuple('Meeting', ['begin', 'end'])

n = int(input())
a = [Meeting(*map(int, input().split())) for _ in range(n)]
a.sort(key=lambda x: (x.end, x.begin)) #end로 정렬하고 같을 경울
now = 0 #회의가 끝난 시간
ans = 0
for p in a:
    if now<= p.begin:
        now = p.end
        ans+=1
print(ans)



