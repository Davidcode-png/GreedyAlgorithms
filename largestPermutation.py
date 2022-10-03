def solve(A,B):
	# A - Array
	# B - No of Permutation
	i = 0
	_max = len(A) # Keeps the track of the current N
	d = {x : i for i,x in enumerate(A)} # Tells us where each element is 

	while B and i < len(A):
		j = d[_max]
		if i == j:
			pass
		else:
			B -= 1
			A[i],A[j] = A[j],A[i]
			d[A[i]], d[A[j]] = d[A[j]] , d[A[i]]

		i += 1
		_max -= 1

	return A

A = [3,1,4,5,2,6]
print(solve(A,3))