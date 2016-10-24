def makeLPSArray(pat):
	m = len(pat)
	i = 1
	j = 0
	lps = [0]
	l = 0
	while i<m:
		if pat[i]==pat[l]:
			l+=1
			lps.append(l)
			i+=1
		else:
			if l!=0:
				l=lps[l-1]
			else:
				i+=1
				lps.append(0)
	return lps

def kmpSearch(txt,pat):
	n = len(txt)
	m = len(pat)
	lps = makeLPSArray(pat)
	indexes = []
	i = 0
	j = 0
	while i<n:
		if txt[i]==pat[j]:
			i+=1
			j+=1
		if j==m:
			indexes.append(i-j)
			j = lps[j-1]
		elif i<n and txt[i]!=pat[j]:
			if j!=0:
				j = lps[j-1]
			else:
				i+=1
	return indexes

if __name__=="__main__":
	s = raw_input("Enter the String: ")
	p = raw_input("Enter the Pattern: ")
	print kmpSearch(s,p)
