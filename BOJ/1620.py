import sys
input = sys.stdin.readline
N, M = map(int, input().split())
#최대 길이는 20, 최소 길이는 2야
pkmn = []
pkmn_dic = dict()
for i in range(1, N+1):
    pk=input().rstrip()
    pkmn.append(pk)
    pkmn_dic[pk] = i #인덱스 저장

for _ in range(M):
    query = input().rstrip()
    if query in pkmn_dic:
        print(pkmn_dic[query])
    else:
        print(pkmn[int(query)-1])