#포스트오더의 가장 마지막은 루트
INF = 100000
inorder = [0] * INF
postorder = [0] * INF
position = [0] *(INF+1) #인오더에서 i번 정점의 순서 inorder[position[i]] = i

def solve(in_start, in_end, post_start, post_end):
    if in_start>=in_end or post_start>post_end:
        return
    root = postorder[post_end]
    print(root) #프리오더 출력
    p = position[root] #루트의 인오더에서 위
    left = p-in_start
    solve(in_start, p-1, post_start, post_start+left-1)#Left tree
    solve(p+1, in_end, post_start+left, post_end-1)# Right Tree