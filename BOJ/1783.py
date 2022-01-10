from sys import stdin

input = stdin.readline

n, m = map(int(input()))

if n==1:
    print(1)
elif n==2:
    print(min(4, (m+1)//2))
elif n>=3:
    if m>=7:
        print(m-2) ## 우로 2칸을 2번만 이동하면 나머지는 계속 우로 1칸씩만 이동 가능
    else:
        print(min(4, m ))


#높이가 1인경우 경우의 수 없음
#높이가 2인경우 횟수 4회 초과시 이동불가이므로 min(4, (width+1)/2)
#높이가 3이상인 경우 너비가 7이상이 개수 제한이 없고, 이 때 정답은 width-2
#너비가 7 미만이면 정답은 min(4, width)
# if n ==1:
#     print(1)
# elif n==2:
#     print(min(4, (m-1)//2+1))
# elif n>=3:
#     if m>=7:
#         print(m-2)
#     else:
#         print(min(4, m))