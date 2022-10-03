def solve(A):
	A = sorted(A)
	score = 1
	new_array = []
	# new_array.append(score)
	print(A)
	for i,j in enumerate(range(1,len(A))):
		if A[i] < A[j]:
			score += 1
		elif A[i] > A[j]:
			score = 1
		else:
			score = score
		print(A[i],A[j],score)

		new_array.append(score)
	print(new_array)
	return sum(new_array)

A = [1,2,7,4,3,3,1]

print(solve(A))