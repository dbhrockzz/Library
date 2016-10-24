d = 256
#q -> prime number
def RKSearch(pat,txt,q=101):
	m = len(pat)
	n = len(txt)
	i = 0
	j = 0
	p = 0
	t = 0
	h = pow(d,m-1,q)
	indexes = []

	for i in xrange(m):
		p = (d*p + ord(pat[i]))%q
		t = (d*t + ord(txt[i]))%q
	#print p,t
	for i in xrange(n-m+1):
		if p==t:
			for j in xrange(m):
				if txt[i+j]!=pat[j]:
					break
			if j==m-1 and txt[i+j]==pat[j]:
				indexes.append(i)

		if i<n-m:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+m]))%q
			if t<0:
				t=t+q

	return indexes

if __name__=="__main__":
	s = raw_input("Enter the String: ")
	p = raw_input("Enter the Pattern: ")
	print RKSearch(p,s)
