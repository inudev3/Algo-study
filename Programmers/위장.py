from collections import defaultdict
def solution(clothes):
    hash=defaultdict(int)
    for cloth in clothes:
        hash[cloth[1]]+=1
    ans=1
    for item in hash.items():
        ans*=(item[1]+1)
    return ans-1