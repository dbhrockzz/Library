import sys

def minCoins(den,tot):
    mini = [sys.maxint]*(tot+1)
    mini[0] = 0
    track = [0]*(tot+1)
    for i in range(1,tot+1):
        for c in den:
            if c<=i and mini[i-c]+1<mini[i]:
                mini[i] = mini[i-c]+1
                track[i] = i-c
    ans = []
    ind = tot
    ans.append(ind-track[ind])
    while track[ind]!=0:
        ind = track[ind]
        ans.append(ind-track[ind])
    return mini[tot],ans

if __name__=="__main__":
    den = map(int,raw_input("Denominatins : ").strip().split())
    amt = input("Amount Required: ")
    a,b = minCoins(den,amt)
    print 'Minimum No. Coins: ',a
    print 'Solution: ',b