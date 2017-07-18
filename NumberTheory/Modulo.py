import sys
sys.setrecursionlimit(10**9)
def expo(x,n):
    if n==0: return 1
    ans = 1
    while n>0:
        if n&1:
            ans = ans*x
        x *= x
        n /= 2
    return ans

def modexpo(x,n,m):
    if n==0: return 1
    ans = 1
    while n>0:
        if n&1:
            ans = (ans*x)%m
        x = (x*x)%m
        n /= 2
    return ans%m


def gcd(a,b):
    while b!=0:
        a,b = b,a%b
    return a

import sys
sys.setrecursionlimit(10**9)
def exteuc(a,b):
    if b==0:
        return 1,0
    x,y = exteuc(b,a%b)
    return y,x-(a/b)*y

def modinv(a,m):
    x,y = exteuc(a,m)
    return x%m

def modinvprime(a,m):
    return modexpo(a,m-2,m)

