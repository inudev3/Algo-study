n, s = map(int, input().split())

def go(index, sum):
    if index==n:
        if sum==s:
            return 1
        else:
            return 0
    go(index+1, )