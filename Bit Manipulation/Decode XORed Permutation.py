def decode(self, encoded: List[int]) -> List[int]:
	N = len(encoded) + 1
	X = 1
	for i in range(2, N + 1):
		X ^= i
	for i in range(1, N, 2):
		X ^= encoded[i]
	perm = [X]
	for i in range(1, N):
		perm += [perm[i - 1] ^ encoded[i - 1]]
	return perm