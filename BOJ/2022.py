 # c = (h1*h2)/(h1+h2)
 import math
 # x = root(h1**2+ d**2), y = root(h2**2+d**2)
 #d가 증가하면 c는 줄어들고 d가 감소하면 c는 늘어나므로 이를 이용해 이분탐색
 #실수의 이분탐색은 어떻게 해야할까?
 #left = mid, right= mid가 되야함
 # while left<=right은 쓸 수 없으므로 아래의 둘 중 하나를 사용해야함
 # for k in range(10000) 이분탐색을 만 번 하면 범위는 1/2**10000이므로 소수점 자리 이하의 작은 단위
 #while(abs(right-left)>1e-6) 소수점 6자리보다 작아질 때까지 반복
 #위 문제에선 소수점 3째자리이므로 좀 더 함

 x,y,c = map(float, input().split())
 left = 0
 right = min(x,y)

 while abs(right-left)>1e-6:
# for _ in range(10000):
     mid = (left+right)/2
     d = mid
     h1 = math.sqrt(x*x-d*d)
     h2 = math.sqrt(y*y-d*d)
     h = (h1*h2)/(h1+h2)
     if h>c:
         left = mid
     else:
         right =mid
print(left)


