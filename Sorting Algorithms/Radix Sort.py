def counting_sort(List, exp):
	N = len(List)
	res = [0] * N
	count = [0] * 10

	for i in range(N):
		ind = List[i] // exp
		count[ind % 10] += 1

	for i in range(1, 10):
		count[i] += count[i - 1]

	i = N - 1
	while i >= 0:
		ind = List[i] // exp
		res[count[ind % 10] - 1] = List[i]
		count[ind % 10] -= 1
		i -= 1
	
	for i in range(N):
		List[i] = res[i]

def radix_sort(List):
	max_ = max(List)
	exp = 1
	while max_ / exp > 1:
		counting_sort(List, exp)
		exp *= 10

L = [5, 4, 6, 3, 1, 2]
radix_sort(L)
print(L)
