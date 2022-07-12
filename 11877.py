import itertools

n, x = map(int, input().split())
heights = [i for i in range(1,n+1)]
ans= False
for histogram in itertools.permutations(heights):
    Sum = 0
    stack =[]
    for i in range(1, n-1):
        if histogram[i]>histogram[i-1] or histogram[i]>histogram[i+1]:
            continue
        water = min(histogram[i+1]-histogram[i], histogram[i-1]-histogram[i])
        stack.push(water)
    if Sum==x:
        print(*histogram)
        exit()

print(-1)

