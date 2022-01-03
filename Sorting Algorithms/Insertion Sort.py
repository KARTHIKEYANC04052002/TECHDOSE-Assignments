def insertion_sort(List):
    N = len(List)
    for i in range(1, N):
        key = List[i]
        j = i - 1
        while j >= 0 and key < List[j]:
            List[j + 1] = List[j]
            j -= 1
        List[j + 1] = key
    return List

L = [1, 2, 5, 3, 6, 8, 7]
print(insertion_sort(L))
