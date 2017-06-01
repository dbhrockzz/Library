def mvcs(arr):
    n = len(arr)
    ans = [0]*n
    if arr[0]>0:
        ans[0] = arr[0]
    for i in range(1,n):
        if arr[i]+ans[i-1] > 0:
            ans[i] = arr[i]+ans[i-1]
        else:
            ans[i] = 0
    return max(ans)

if __name__=="__main__":
    arr = map(int,raw_input("Enter the array : ").strip().split())
    print "Maximum Contiguous Value Sum:",mvcs(arr)