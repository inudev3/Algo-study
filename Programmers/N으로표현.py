def solution(N, number):
    def getNs(N, idx):
        result = N
        for i in range(idx):
            result *=10
            result+=N
        return result
    if N==number: return 1
    DP = [set() for _ in range(9)] #k개의 N으로 만들 수 있는 숫자의 개수
    DP[0].add(N) #1개
    for k in range(1,8):
        DP[k].add(getNs(N, k))
        for i in range(k):
            for j in range(k):
                if i+j+1!=k: continue
                for a in DP[i]:
                    for b in DP[j]:
                        DP[k].add(a+b)
                        if a>b:
                            DP[k].add(a-b)
                        DP[k].add(a*b)
                        if a//b >0:
                            DP[k].add(a//b)
        if number in DP[k]:
            return k+1
    return -1