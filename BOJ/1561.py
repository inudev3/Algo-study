n, m = map(int, input().split())

a = list(map(int, input().split()))

#x분까지 탑생한 학생의 수는
# cnt=m
# for i in range(n):
#     cnt+= x//a[i]

#결국 n번째 학생이 타는 놀이기구의 번호를 찾는 문제
#시간을 결정하면 특정한 학생이 타는 기구의 번호를 찾을 수 있음
if n<=m:
    print(n) #놀이기구의 수보다 학생의 수가 작으면 0분에 모두 타게됨

left = 0 ##탑승시간을 이분탐색
right =  2000000000*10000*30 #시간의 최대값 - 학생의 수 * 놀이기구의 수 *탑승시간