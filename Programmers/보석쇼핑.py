from collections import defaultdict


def solution(gems):
    answer = [0, 0]
    shortest = len(gems) + 1
    candidates = []
    start, end = 0,0
    kinds = len(set(gems))
    current = defaultdict(int)

    while True:
        if start == len(gems):
            break
        if len(current) == kinds:
            candidates.append((start, end))
            current[gems[start]] -= 1
            if current[gems[start]] == 0:
                del current[gems[start]]
            start += 1
            continue
        if end == len(gems):
            break
        if len(current) != kinds:
            current[gems[end]] += 1
            end += 1
            continue

    for s, e in candidates:
        if e - s < shortest:
            shortest = e - s
            answer[0] = s + 1
            answer[1] = e
    return answer

from collections import defaultdict


def solution(gems):
    bag = defaultdict(int)
    left,right = 0, 0
    least = len(set(gems))
    ans = []
    while True:
        if left==len(gems):
            break
        if len(bag)==least:
            ans.append((left,right))
            bag[gems[left]]-=1
            if bag[gems[left]]==0:
                del bag[gems[left]]
            left+=1
            continue
        if right==len(gems):
            break
        if len(bag)<least:
            bag[gems[right]]+=1
            right+=1
            continue
    print(ans)
    ans = sorted(ans, key=lambda x:(x[1]-x[0]+1, x[0]))
    print(ans)
    return [*ans]

print(solution(["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]))

