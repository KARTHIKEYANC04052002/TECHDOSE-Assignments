def hammingDistance(self, x: int, y: int) -> int:
	x = x ^ y
	Dis = 0
	while x:
		x &= x - 1
		Dis += 1
	return Dis