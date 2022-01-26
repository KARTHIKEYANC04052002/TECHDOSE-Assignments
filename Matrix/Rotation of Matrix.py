def rotateMatrix(mat, R, C):
	top = 0
	bottom = R - 1
	left = 0
	right = C - 1

	while left < right and top < bottom:
		prev = mat[top + 1][left]
		for i in range(left, right + 1):
			mat[top][i], prev = prev, mat[top][i]
		top += 1
		for i in range(top, bottom + 1):
			mat[i][right], prev = prev, mat[i][right]
		right -= 1
		for i in range(right, left - 1, -1):
			mat[bottom][i], prev = prev, mat[bottom][i]
		bottom -= 1
		for i in range(bottom, top - 1, -1):
			mat[i][left], prev = prev, mat[i][left]
		left += 1
	return mat
