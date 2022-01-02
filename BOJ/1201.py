# N의 최소길이는 M+K-1이며(최대 한개의 정수를 공유)
# N의 최대길이는 MK이다. (비둘기 집의 원리에 의해) MK개의 수가 있다면 길이가 M+1이나 K+1인 수열을 반드시 만들 수 있게 되기 때문
# 수열을 M개의 그룹으로 나누고,적어도 하나의 그룹의 길이는 K로 만든뒤 뒤집으면, 증가하는 부분수열의 길이가 M이되고 감소하는 부분수열의 길이가 K가 된다.

n, m, k = map(int, input().split())
if m + k - 1 <= n <= m * k:
    a = [i + 1 for i in range(n)]
    g = []
    g.append(0)  # 그룹이 나뉘는 인덱스 저장
    g.append(k)
    n -= k
    m -= 1
    gs = 1 if m == 0 else n / m
    r = 0 if m == 0 else n % m
    for i in range(m):
        g += [g[-1] + gs + (1 if r > 0 else 0)]  ##그룹의 크기만큼 더해주고 나머지가 있다면 1을 더해줌
        if r > 0:
            r -= 1
    for i in range(len(g)-1):
        u = g[i]
        v = g[i+1]
        a[u:v] = a[u:v][::-1]#뒤집어준다
    print(' '.join(map(str, a)))
else:
    print(-1)
