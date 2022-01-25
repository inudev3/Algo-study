n= int(input())
D = [0]* (n+1)
D[0] = 0
D[1] = 0
for i in range(2, n):
    D[i]+= 3*D[i-2]
    for j in range(4, n, 2):
        D[i] += 2*D[i-j]