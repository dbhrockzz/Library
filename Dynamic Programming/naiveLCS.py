def lcs(a,b):
	"""naive implementation of lcs problem
	returns the length of lcs 
	Complexity O(2^n)"""
	n = len(a)
	m = len(b)
	if n==0 or m==0:
		return 0
	if a[-1]==b[-1]:
		return 1+lcs(a[:n-1],b[:m-1])
	else:
		return max(lcs(a,b[:m-1]),lcs(a[:n-1],b))

if __name__=="__main__":
	s1 = raw_input("Enter string 1: ")
	s2 = raw_input("Enter string 2: ")
	print lcs(s1,s2)
