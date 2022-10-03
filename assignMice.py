def solve(A,B):
	A.extend(B)
	A = sorted(A)
	minutes = []
	n = len(A)
	for i in range (0,n,2):
		x = A[i+1] - A[i]
		minutes.append(x)
	return max(minutes)

A = [3,2,-4]
B = [0,-2,4]
print(solve(A,B))