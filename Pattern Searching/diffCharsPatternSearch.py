#Assumes that pattern has no repeated characters

def search(pat,txt):
	n = len(txt)
	m = len(pat)
	i = 0
	indexes = []
	while i<=(n-m):
		
		for j in range(m):
			if txt[i+j]!=pat[j]:
				break
		if j==m-1 and txt[i+j]==pat[j]:
			indexes.append(i)
			i+=m
		elif j==0:
			i+=1
		else:
			i+=j
	return indexes

if __name__=="__main__":
	s = raw_input("Enter the string: ")
	p = raw_input("Enter the pattern: ")
	print search(p,s)
