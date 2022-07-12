# v,e = map(int, input().split())
# graph = [[] for _ in range(e)]
# parent = list(range(v+1))
# for i in range(e):
#     a,b,c = map(int, input().split())
#     graph[i].extend([c,a,b])
# graph.sort(key=lambda x:x[0]) ##비용으로 정렬
# def Find(x):
#     if x==parent[x]:
#         return x
#     parent[x] = Find(parent[x])
#     return parent[x]
# def Union(x,y):
#     x = Find(x)
#     y = Find(y)
#     if x==y:
#         return
#     parent[x] = y
# ans = 0
# for i in range(e):
#     cost,a,b = graph[i]
#     x = Find(a)
#     y = Find(b)
#     if x!=y:
#         Union(x,y)
#         ans+=cost
# print(ans)
n = int(input())
card = list(map(int, input().split()))
m = int(input())
num = list(map(int, input().split()))
card.sort()
start = 0
end = n - 1


def binarySearch(num):
    while start < end:
        mid = (start + end) // 2
        if num == card[mid]:
            return mid
        elif num < card[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1


for i in num:
    res = binarySearch(i)
    print(1 if res != -1 else 0, end=' ')
