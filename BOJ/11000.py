n = int(input())
Lect = []
for _ in range(n):
    Lect.append(map(int, input().split()))
Lect.sort(key=lambda x:x[1])

starts = [i for i,j in Lect]
ends = [j for i,j in Lect]
cnt=0
for end in ends:
    for j in range(n):
        if starts[j]<end:
            cnt+=1
        else:
            break