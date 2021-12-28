N, M = map(int, input().split())
#최대 길이는 20, 최소 길이는 2야
pkmn = []
pkmn_dic = {}
for i in range(N):
    pk=input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i+1 #인덱스 저장

for _ in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(pkmn[int(query)])
    else:
        print(pkmn_dic[query])