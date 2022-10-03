def bulbs(A):
	cost = 0
	for b in A:
		if cost % 2 == 0:
			b = b
		else:
			b = not b

		if b % 2 == 1:
			continue
		else:
			cost += 1
	return cost

bulb = [0,1,0,1,1,0,1,1]
print(bulbs(bulb))