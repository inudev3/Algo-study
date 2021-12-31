from sys import stdin
N, K = map(int, stdin.readline())
words = [input() for _ in range(N)]
learn = [False] * 26
for _ in range(N):
    s = stdin.readline()
    for char in s:
        words |= (1<<(char-'a')) # 알파벳을 숫자로 치환한 값을 집합에 더해줌. 일종의 set

def count( words):

def go(index, k , words): # 알파벳의 인덱, 배워야할 단어의 개수, mask는 배운 알파벳의 비트마스트(집합), words
    if k<0:
        return 0 #배울 수 있는 단어 0개
    if index==26: #알파벳 26개의 인덱스
        return count(words) #배운 알파벳으 읽을 수 있는 단어 개수 리턴
    ans = 0
    t1 = go(index+1, k-1, words) #26개의 알파벳 중 index번째를 배우기로 선택한 경우
    if ans<t1:
        ans = t1
    if index not in [ord('a')-ord('a'), ord('n')-ord('a'), ord('t')-ord('a'), ord('i')-ord('a'), ord('c')-ord('a')]:
        #알파벳이 무조건 포함되는 antic에 속하지 않는다면
        t1
