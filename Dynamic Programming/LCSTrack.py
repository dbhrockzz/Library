def lcs(a,b):
    """Longest Common Subsequence using Dynamic Programming Approach
	Returns Length of the LCS
	Complexity O(m*n) """
    m = len(a)
    n = len(b)
    l = [[None]*(n+1) for i in range(m+1)]

    for i in range(m+1):
        for j in range(n+1):
            if i==0 or j==0:
                l[i][j] = 0
            elif a[i-1]==b[j-1]:
                l[i][j]=l[i-1][j-1]+1
            else:
                l[i][j]=max(l[i-1][j],l[i][j-1])
    ans = l[m][n]
    anslist = []
    r = m
    c = n
    #print l
    while r>0 and c>0:
        #print r,c
        if a[r-1]==b[c-1]:
            print r,c
            anslist.insert(0,a[r-1])
            r-=1
            c-=1
        elif l[r-1][c]>=l[r][c-1]:
            r-=1
        else:
            c-=1
    return l[m][n],"".join(anslist)


if __name__=="__main__":
    s1 = raw_input("Enter string 1: ")
    s2 = raw_input("Enter string 2: ")
    l,s = lcs(s1,s2)
    print "Length LCS:",l
    print "LCS:",s
