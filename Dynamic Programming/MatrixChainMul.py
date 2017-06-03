import sys
def mul(dims):
    """ returns minimum cost possible """
    d = len(dims)
    m = [[0]*d for i in range(d)]
    for cl in range(2,d):
        for i in range(1,d-cl+1):
            j = i+cl-1
            m[i][j] = sys.maxint
            for k in range(i,j):
                m[i][j] = min(m[i][j],m[i][k]+m[k+1][j]+dims[i-1]*dims[k]*dims[j])
    return m[1][d-1]

if __name__=="__main__":
    arr = map(int,raw_input("Enter the dimensions: ").strip().split())
    print "Cost:",mul(arr)