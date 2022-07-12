##unionfind

def solution(enroll, referral, seller, amount):
    parent = {c:p for c,p in zip(enroll,referral)}
    ans = {c:0 for c in enroll}
    for s, m in zip(seller,amount):
        m*=100
        while s in parent and m>0:
            ans[s]+=m-int(m*0.1)
            m = int(m*0.1)
            s = parent[s]
    return list(ans.values())


def solution(enroll, referral, seller, amount):
    ans = {c: 0 for c in enroll}
    parent = dict(zip(enroll, referral))
    for s, m in zip(seller, amount):
        m *= 100
        while s != "-" and m > 0:
            ans[s] += m - m // 10
            m //= 10
            s = parent[s]
    return list(ans.values())
