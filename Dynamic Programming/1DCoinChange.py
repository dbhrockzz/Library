import sys

def minCoins(den,tot):
    mini = [sys.maxint]*(tot+1)
    mini[0] = 0
    for i in range(1,tot+1):
        for c in den:
            if c<=i:
                mini[i] = min(mini[i-c]+1,mini[i])
    return mini[tot]

if __name__=="__main__":
    den = map(int,raw_input("Denominatins : ").strip().split())
    amt = input("Amount Required: ")
    print 'Minimum No. Coins: ',minCoins(den,amt)