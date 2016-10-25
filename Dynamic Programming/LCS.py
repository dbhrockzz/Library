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
	return l[m][n]

if __name__=="__main__":
	s1 = raw_input("Enter string 1: ")
	s2 = raw_input("Enter string 2: ")
	print lcs(s1,s2)
