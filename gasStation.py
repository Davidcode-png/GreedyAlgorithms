def solve(A,B):
	n = len(A)
	curr = start = 0
	for i, (g,c) in enumerate(zip(A*2,B*2)):
		if i == start + n:
			return start
		curr += g - c
		if curr < 0:
			start = i + 1
			curr = 0
	return -1
A = [3,5,2,1,7]
B = [4,2,1,9,1]
print(solve(A, B))