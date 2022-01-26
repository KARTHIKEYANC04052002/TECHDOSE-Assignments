def spiralTraversalMatrix(mat, R, C):
    st_r = 0
    en_r = R
	st_c = 0
	en_c = C

	while st_r < en_r and st_c < en_c:
		for i in range(st_c, en_c):
			print(mat[st_r][i], end=' ')
		st_r += 1
		for i in range(st_r, en_r):
			print(mat[i][en_c - 1], end=' ')
		en_c -= 1
		if st_r < en_r:
			for i in range(en_c - 1, st_c - 1, -1):
				print(mat[en_r - 1][i], end=' ')
			en_r -= 1
		if st_c < en_c:
			for i in range(en_r - 1, st_r - 1, -1):
				print(mat[i][st_c], end=' ')
			st_c += 1
