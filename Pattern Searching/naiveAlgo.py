def search(pat,txt):
	m = len(pat)
	n = len(txt)
	indexes = []
	for i in xrange(n-m+1):
		for j in xrange(m):
			#print i,j
			if txt[i+j]!=pat[j]:
				break
		if j==m-1 and txt[i+j]==pat[j]:
			indexes.append(i)
	return indexes

if __name__=="__main__":
	s = raw_input("Enter the string: ")
	p = raw_input("Enter the pattern: ")
	print search(p,s)
