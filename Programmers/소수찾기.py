import itertools
import math


def isPrime(num):
    if num == 0 or num == 1:
        return False
    lim = int(math.sqrt(num))
    for i in range(2, lim + 1):
        if num % i == 0:
            return False
    return True


## 순열은 dfs
def dfs(ans, checked, nums, current):
    if len(current) == len(nums):
        ans.add(int(current))
        return
    else:
        for i in range(len(nums)):
            if not checked[i]:
                checked[i] = True
                current += str(nums[i])
                dfs(ans, checked, nums, current)
                checked[i] = False
                current = current[:-1]



def solution(numbers):
    nums = list(map(int, numbers))
    ans = set()
    for i in range(1, len(numbers) + 1):
        for j in itertools.permutations(numbers, i):
            num = int("".join(j))
            if isPrime(num):
                ans.add(num)
    return len(ans)

print(solution("17"))
