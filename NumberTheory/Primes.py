def checkPrime(n):
    if n==2:
        return True
    if n%2==0:
        return False
    i=3
    while i*i<=n:
        if n%i==0: return False
        i+=2
    return True

def sieve(n):
    isPrime = [True]*(n+1)
    isPrime[0] = False
    isPrime[1] = False
    i = 2
    while i*i<=n:
        if isPrime[i]:
            for j in range(i*i,n+1,i):
                isPrime[j] = False
        i+=1
    return isPrime

def factorize(n):
    res = []
    i = 2
    while i*i<=n:
        while n%i==0:
            res.append(i)
            n/=i
        i+=1
    if n!=1: res.append(n)
    return res

def factors(n):
    minPrime = [0]*(n+1)
    i = 2
    while i*i<=n:
        if minPrime[0]==0:
            for j in range(i*i,n+1,i):
                if minPrime[j]==0:
                    minPrime[j] = i
        i+=1
    for i in range(2,n+1):
        if minPrime[i]==0:
            minPrime[i] = i
    return minPrime

def primefactors(n):
    res = []
    minPrime = factors(n)
    while n!=1:
        res.append(minPrime[n])
        n/=minPrime[n]
    return res
    