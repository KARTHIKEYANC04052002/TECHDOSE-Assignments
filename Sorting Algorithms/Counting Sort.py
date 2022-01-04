def counting_sort(List):
	max_val = int(max(List))
	min_val = int(min(List))
	total = max_val - min_val + 1
	
	count_ = [0 for i in range(total)]
	res = [0 for i in range(len(List))]
	
	for i in range(len(List)):
		count_[List[i] - min_val] += 1
	
	for i in range(1, total):
		count_[i] += count_[i-1]
	
	for i in range(len(List)-1, -1, -1):
		res[count_[List[i] - min_val] - 1] = List[i]
		count_[List[i] - min_val] -= 1

	return res

L = [5, 4, 6, 3, 1, 2]
print(counting_sort(L))