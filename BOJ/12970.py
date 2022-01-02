n, k = map(int, input().split())
for a in range(n+1):
    b = n-a
    if a*b <k : continue
    cnt = [0] * (b+1) #b를 먼저 전부 놓는다고 생각하고 , a가 몇번 b의 위치에 추가되야하는지를 세기위한 배
    for i in range(a):
        x = min(b,k) #한번에 최대 b개 만큼 빼줄 수 있음
        cnt[x] +=1 #해당 위치 a의 개수 증가
        k-=x # k를 계속 b개만큼 줄여나간다.
    for i in range(b, -1, -1):
        for j in range(cnt[i]):
            print('A')
        if i>0: # i가 0이면 A로 끝
            print('B')
    print()
print