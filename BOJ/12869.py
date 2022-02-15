import itertools

D =[[[0]*61 for _ in range(61)] for _ in range(61])
def go(i,j,k):
    if i<0:
        return go(0,j,k)
    if j<0:
        return go(i,0,k)
    if k<0:
        return go(i,j,0)
    if i==0 and j==0 and k==0:
        return 0
    ans = D[i][j][k]
    if ans!=-1:
        return ans
    ans = 10000000
    p = [1,3,9]
    while itertools.permutations(p, 3):
        if ans> go(i-p[0], j-p[1], k-p[2]):
            ans = go(i-p[0], j-p[1], k-p[2])
    ans+=1
