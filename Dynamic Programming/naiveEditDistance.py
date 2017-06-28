def editDistance(a,b):
	"""naive Implementation of calculating the Edit Distance
	Complexity is Exponential"""
	n = len(a)
	m = len(b)

	if m==0:
		return n
	elif n==0:
		return m
	else:
		if a[-1]==b[-1]:
			return editDistance(a[:n-1],b[:m-1])
		else:
			return 1+min(editDistance(a[:n-1],b[:m]),editDistance(a[:n],b[:m-1]),editDistance(a[:n-1],b[:m-1]))

if __name__ == "__main__":
	s1 = raw_input("Enter String 1: ")
	s2 = raw_input("Enter String 2: ")
	print "Edit Distance : ",editDistance(s1,s2)