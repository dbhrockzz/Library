def LIS(arr):
	""" returns length of Longest Increasing Subsequence"""
	n = len(arr)
	l = [1]*n

	for i in xrange(1,n):
		for j in xrange(i):
			if arr[i]>arr[j] and l[i]<l[j]+1:
				l[i]=l[j]+1
	return max(l)

if __name__=="__main__":
	s = raw_input("Enter the space separated array: ").strip().split()
	print LIS(s)

