import heapq

n = int(input())

l = []
r = []
while n:
    x = int(input())
    if not l or not r:
        heapq.heappush(l, -x) #최대힙
    else:
        if x<= -l[-1]:
            heapq.heappush(l,-x)
        elif x>= r[-1]:
            heapq.heappush(r, x)
        else:
            heapq.heappush(l, -x)
    while not (len(l) == len(r) or len(l)==len(r)+1) :
        if len(r) > len(r):
            r.append(-l[-1])
            l.pop()
        else:
            l.append(r[-1])
            r.pop()
    print(l[-1])