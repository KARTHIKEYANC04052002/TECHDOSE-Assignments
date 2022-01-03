def selection_sort(List):
    N = len(List)
    for i in range(N - 1):
        min_val, min_ind = List[i], i
        for j in range(i + 1, N):
            if List[j] < List[i]:
                min_val = List[j]
                min_ind = j
        List[i], List[min_ind] = List[min_ind], List[i]
    return List

L = [1, 2, 5, 3, 6, 8, 7]
print(selection_sort(L))