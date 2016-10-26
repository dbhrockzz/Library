def editDistance(a,b):
	"""Calculating Edit Distance using Dynamic Programming Approach
	Complexity = O(m*n)"""
	n = len(a)
	m = len(b)
	l = [[None]*(n+1) for i in range(m+1)]

	for i in range(m+1):
		for j in range(n+1):
			if i==0 or j==0:
				l[i][j]=0
			elif b[i-1]==a[j-1]:
				l[i][j]=l[i-1][j-1]
			else:
				l[i][j] = 1+min(l[i-1][j],l[i][j-1],l[i-1][j-1])
	return l[m][n]

if __name__ == "__main__":
	s1 = raw_input("Enter String 1: ")
	s2 = raw_input("Enter String 2: ")
	print "Edit Distance : ",editDistance(s1,s2)