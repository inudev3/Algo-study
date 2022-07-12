from collections import defaultdict, Counter
def solution(genres, plays):
    hash=defaultdict(list)
    songs  = list(zip(genres, plays))
    res =[]
    ans=[]
    for i in range(len(songs)):
        genre, play = songs[i]
        hash[genre].append((play,i))
    for genre in hash:
        hash[genre] = sorted(hash[genre], key=lambda x:x[0], reverse=True)
    sorted_dict = sorted(hash.items(), key=lambda x:sum(i[0] for i in x[1]), reverse=True)
    # [("클래식", [(500,0), (150,2)]), ('팝', [(600, 1),(2500,4)])]
    res = sorted(res, key=lambda x:x[0], reverse=True)
    genre, rest = zip(*sorted_dict)
    for rst in rest:
        ans.extend(rst[:2])
    ans = [i[1] for i in ans]
    return ans