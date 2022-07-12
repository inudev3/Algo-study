n = int(input())

D = [0 for _ in range(n+1)]
for i in range(1, n+1):
    D[i] = i
    for j in range(int(i**0.5)+1):
        if D[i]> D[i-j**2]+1:
            D[i] = D[i-j**2]+1
print(D[n])