from bisect import bisect_right as upper_bound
MAX = 1000
def binaryMedian(mat, r, c):
	mi = mat[0][0]
	mx = 0
	for i in range(r):
		if mat[i][0] < mi:
			mi = mat[i][0]
		if mat[i][c-1] > mx :
			mx = mat[i][c-1]
	desired = (r * c + 1) // 2
	while mi < mx:
		mid = mi + (mx - mi) // 2
		place = 0

		for i in range(r):
			j = upper_bound(mat[i], mid)
			place = place + j
		if place < desired:
			mi = mid + 1
		else:
			mx = mid
	return mi
