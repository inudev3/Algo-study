import collections

T = int(input())
for _ in range(T):
    k,m,p = map(int,input().split())
    graph  = [[] for _ in range(m+1)]
    indegree = [0 for _ in range(m+1)]
    DP = [[0,0] for _ in range(m+1)]
    max_order =-1
    max_cnt = -1
    for i in range(p):
        a, b = map(int, input().split())
        graph[a].append(b)
        indegree[b]+=1
        queue = collections.deque()
        for i in range(1,m+1):
            if indegree[i][0]==0:
                queue.append(i)
        while queue:
            now = queue.popleft()
            for next in graph[now]:
                indegree[next]-=1
                if indegree[next]==0:
                    queue.append(next)
                if Strahler[next][1] ==0:
                    Strahler[next][0] = Strahler[now][0]
                elif Strahler[next][0]<Strahler[now][0]:
                    Strahler[next] = Strahler[now]
                elif Strahler[next][0]==Strahler[now][0] and S
                    if Strahler[next]==Strahler[now]:
                        Strahler[next]+=1
                    elif Strahler[next]<Strahler[now]:









    print(Strahler[m])
