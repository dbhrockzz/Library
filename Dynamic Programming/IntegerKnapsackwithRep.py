def knap(weight,values,n,M):
    """
    weight -> Weights of n items
    values -> values of n items
    n -> number of items
    M -> maximum Weight allowed
    """
    assert len(weight)==n
    assert len(values)==n

    arr = [0]*(M+1)
    for i in range(1,M+1):
        arr[i] = arr[i-1]
        for j in range(n):
            if weight[j]<=i:
                arr[i] = max(arr[i],arr[i-weight[j]]+values[j])
    return arr[M]

if __name__=="__main__":
    n = input("Enter the number of items: ")
    wts = map(int,raw_input("Enter the weights : ").strip().split())
    vls = map(int,raw_input("Enter the values : ").strip().split())
    M = input("Enter the maximum weight allowed : ")
    print "Maximum Value Possible:",knap(wts,vls,n,M)
