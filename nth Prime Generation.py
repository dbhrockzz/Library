primes = [0,2,3,5,7,11,13,17,19,23,29]

def check(a,l):
    for x in l[1:]:
        if a%x==0:
            return False
    return True
def prime(n):
    if len(primes)>n:
        return primes[n]
    else:
        while len(primes)<=n:
            temp = primes[-1]+1
            while not check(temp,primes):
                temp+=1
            primes.append(temp)
    return primes[n]

