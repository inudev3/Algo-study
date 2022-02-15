
def prime_list(n):
    sieve = [True]*n #체
    m = int(n**0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(i+1, n, i):
                sieve[j] = False



