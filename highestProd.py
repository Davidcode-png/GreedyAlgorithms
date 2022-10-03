def highestProd(A):
	A = sorted(A)
	highest3 = A[-3] * A[-2] * A[-1]
	lowesthi = A[0] * A[1] * A[-1]

	return max(highest3, lowesthi)

a = [-5,-2,-1,0,0,3,4,5]
print(highestProd(a))