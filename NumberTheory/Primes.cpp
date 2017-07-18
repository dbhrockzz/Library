#include <bits/stdc++.h>
#define MOD 1000000007
#define MAX 200000
#define ll long long 
#define ull unsigned long long
#define fs0(n) for(int i=0;i<n;i++)
#define fs1(n) for(int i=1;i<n;i++)
#define fsx(x,n) for(int i=x;i<n;i++)
#define fl0(n) for(long long i=0;i<n;i++)
#define fl1(n) for(long long i=1;i<n;i++)
#define flx(x,n) for(long long i=x;i<n;i++)
using namespace std;

template<class T>
bool isPrime(T n){
    if(n==2) return true;
    if(n==1 or n%2==0) return false;
    for(T i=3;i*i<=n;i+=2) if(n%i==0) return false;
    return true;
}

void primes(bool *p){
    for(int i=2;i<=1000000;i++) p[i]=true;
    for(int i=4;i<=1000000;i+=2) p[i]=false;
    for(int i=3;i*i<=1000000;i+=2){
        if(p[i])
            for(int j=i*i;j<=1000000;j++) p[j]=false;
    }
    p[0]=false;
    p[1]=false;
    return;
}

int main(){
    return 0;
}