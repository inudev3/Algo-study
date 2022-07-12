import math

#
def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False
    return True



def go(target, num):
    global ans

    if is_prime_num(num):
        if num*10>=target:
            ans.append(num)
            return
        else:
            for i in range(1,10,2):
                go(target, num*10+i)
    else:
        return



n = int(input())
target = 10**n


ans =[]
for i in range(1,10):
    go(target, i)
print(*ans, sep="\n")