import copy

n = int(input())
w= list(map(int, input().split()))

def go(w):
	if len(w)==2:
		return 0
	ans=0
	for i in range(1,len(w)-1):
		energy = w[i - 1] * w[i + 1]
		b =w[:i]+w[i+1:]
		energy+= go(b)

		if ans<energy:
			ans= energy
	return ans


print(go(w))