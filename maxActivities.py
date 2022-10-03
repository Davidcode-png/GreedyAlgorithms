def solve(A):
	A.sort(key=lambda x:x[1])
	prev_s,prev_e = A[0]
	count = 1
	for s,e in A:
		if s <= prev_e:
			pass
		else:
			prev_e,prev_s = e,s
			count += 1
	return count

A = [[5, 9], [1, 2], [3, 4], [0, 6],[5, 7], [8, 9]]
print(solve(A))
