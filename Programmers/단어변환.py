def check(A ,B):
    cnt=0
    for i in range(len(A)):
        if A[i]!=B[i]:
            cnt+=1
    return cnt==1
ans = 50
def dfs(connected, checked, start, target, cnt):
    global ans
    if start==target:
        return cnt
    checked[start] = True
    for next in range(len(connected[start])):
        if connected[start][next] and checked[next] is False:
            checked[next] = True
            ans = min(ans, dfs(connected, checked, next, target, cnt+1))
    return ans

def solution(begin, target, words):
    words =[begin, *words]

    if target not in words:
        return 0
    connected = [[False for _ in range(len(words))] for _ in range(len(words))]
    checked = [False for _ in range(len(words))]
    dist = [0 for _ in range(len(words))]
    for i in range(len(words)):
        for j in range(i+1, len(words)):
            connected[i][j] = check(words[i],words[j])
    ans = dfs(connected,checked, 0, words.index(target), 0)
    return ans

print(solution("hit",	"cog",	["hot", "dot", "dog", "lot", "log", "cog"]))