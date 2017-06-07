def maxSizeSqSM(mat,n,m):
    table = [[0]*(m) for i in range(n)]
    ans = 0
    for i in range(n):
        table[i][0] = mat[i][0]
        ans = max(mat[i][0],ans)
    for i in range(m):
        table[0][i] = mat[0][i]
        ans = max(mat[i][0],ans)
    for i in range(1,n):
        for j in range(1,m):
            table[i][j] = min(table[i-1][j],table[i-1][j-1],table[i][j-1])+1
            ans = max(table[i][j],ans)
    return ans

if __name__=="__main__":
    n = input("Enter the number of rows: ")
    m = input("Enter the number of cols: ")
    print "Enter the matrix: "
    arr = []
    for i in range(n):
        arr.append(map(int,raw_input().strip().split()))
    print maxSizeSqSM(arr,n,m)
    