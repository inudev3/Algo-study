word = input().rstrip()

n = len(word)

D =  [[False]*(n+1) for _ in range(n+1)]
result = [i for i in range(n+1)]
for i in range(1,n+1):
   D[i][i] = True

for i in range(1, n):
   if word[i]==word[i+1]:
      D[i][i+1] = True

for k in range(2, n):
   for i in range(1, n-k+1):
      j = i+k
      if word[i] ==word[j] and D[i+1][j-1]:
         D[i][j]= True

#result가 최소값 DP배열
for i in range(1,n+1):
   result[i] = min(result[i], result[i-1]+1)
   for j in range(i+1, n+1):
      if D[i][j]:
         result[j] = min(result[j], result[i-1]+1)


