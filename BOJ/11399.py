from sys import stdin

input = stdin.readline
n = int(input())

p = list(map(int, input().split()))
p.sort()
sum = 0
ans = 0
for time in p:
    sum += time
    ans += sum
print(ans)
