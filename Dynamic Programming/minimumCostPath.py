def minCostPath(matrix,m,n):
	"""returns the minimum cost needed to reach a matrix from (0,0) to (m,n)
	Complexity O(mn) """
	r = len(matrix)
	c = len(matrix[0])
	cost = [[0]*c for i in range(r)]
	cost[0][0] = matrix[0][0]
	for i in range(1,n+1):
		cost[0][i] = cost[0][i-1]+matrix[0][i]
	for i in range(1,m+1):
		cost[i][0] = cost[i-1][0]+matrix[i][0]
	for i in range(1,m+1):
		for j in range(1,n+1):
			cost[i][j] = min(cost[i-1][j-1],cost[i-1][j],cost[i][j-1])+matrix[i][j]
	return cost[m][n]

if __name__=="__main__":
	m = input("Enter the number of rows: ")
	n = input("Enter the number of columns: ")
	matrix = []
	print "Enter the Matrix:"
	for i in range(n):
		matrix.append(map(int,raw_input().strip().split()))
	print minCostPath(matrix,m-1,n-1)