N = int(input())
S = [list(map(int, input().split())) for _ in range(N)]
first = []
second = []


def go(index, first, second): #각 사람이 어떤 팀에 들어갈 것인지 결정(매번 인덱스마다) 2^N
    if index == N:
        if len(first) != N // 2:
            return -1
        if len(second) != N // 2:
            return -1
        t1 = 0
        t2 = 0
        for i in range(N // 2):
            for j in range(N // 2):
                t1 += S[first[i]][first[j]]
                t2 += S[second[i]][second[j]]
        diff = abs(t1 - t2)
        return diff
    if len(first) > N // 2:
        return -1
    if len(second) > N // 2:
        return -1
    ans = -1
    t1 = go(index + 1, first + [index], second)
    if ans == -1 or (t1 != -1 and ans > t1):
        ans = t1
    t2 = go(index + 1, first, second + [index])
    if ans == -1 or (t2 != -1 and ans > t2):
        ans = t2
    return ans
##브루트포스에서 경우의수를 만들어 불가능한 경우를 제외하는 것이 백트래킹