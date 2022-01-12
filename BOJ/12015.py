import sys
input = sys.stdin.readline

def lower_bound(a, n , key):
    left= 0
    right = n
    while left<right: #이분 탐색에서 나오는 lower_bound. lower bound는 key 이상이 되는 첫 위치, upper boundsms k 초과가 되는 첫 위
        mid = (left+right)//2
        if key<=a[mid]:
            right = mid
        else:
            left= mid+1
    return left
n = int(input())
a = [0] * n #정답배열
nums = list(map(int, input().split()))
length = 0
for num in nums:
    p = lower_bound(a, length, num)
    a[p] = num
    if length==p: #더 큰 수가 존재하지 않으면 길이를 추가
        length+=1
print(length)