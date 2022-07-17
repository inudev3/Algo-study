#
# decreasing = []
# def go(digit, num):
#     if digit==1:
#         decreasing.append(num)
#     else:
#         for i in range(num%10):
#             go(digit-1, num*10+i)
#
# def backtracking(digit):
#     for i in range(digit-1, 10):
#         go(digit,i)
#
# for i in range(1,11):
#     backtracking(i)
# n = int(input())
#
# if n>= len(decreasing):
#     print(-1)
# else:
#     print(decreasing[n])
import sys
from itertools import combinations

n = int(sys.stdin.readline())

nums = list()               # 모든 감소하는 수
for i in range(1, 11):      #  1~10개의 조합 만들기 (0~9개니깐)
    for comb in combinations(range(0, 10), i):  # 0~9로 하나씩 조합 만들기
        comb = list(comb)
        comb.sort(reverse=True)                     # 해당 조합을 감소하는 수로 변경
        nums.append(int("".join(map(str, comb))))

nums.sort()   # 오름차순

try:
    print(nums[n])
except:     # 인덱스가 넘어가는 경우 -1 출력. 마지막 수 9876543210
    print(-1)

n,k = map(int,input().split())
words = [0]*n
for i in range(n):
    s= input()
    for x in s:##모든 알파벳
        words[i] |= (1<<ord(x)-ord('a'))
def count(mask,words):
    cnt=0
    for word in words:
        if (word & (1<<26)-1-mask)==0:
            cnt+=1
    return cnt
def go(index, k, mask, words):##알파벳을 순회
    if k<0:
        return 0
    if index==26:
        return count(mask,words)
    ans=0
    ans =max(ans, go(index+1, k-1, mask|(1<<index), words))
    if index not in map(lambda x:x-ord('a'),[ord('a'),ord('n'), ord('t'), ord('i'),ord('c')]):##antic은 배우지 않는 선택지가 없음
        ans = max(ans, go(index+1, k, mask, words))
    return ans




