def catNum(n):
    if n==1 or n==0:
        return 1
    if nums[n]!=1:
        return nums[n]
    nums[n]=0
    for i in range(1,n+1):
        nums[n] += catNum(i-1)*catNum(n-i)
    return nums[n]

if __name__=="__main__":
    n = input("Enter the number of Nodes : ")
    nums = [1]*(n+1)    
    print "Number of BSTs possible :",catNum(n)