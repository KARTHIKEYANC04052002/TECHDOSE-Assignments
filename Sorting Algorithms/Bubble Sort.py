def bubble_sort(List):
    N = len(List)
    for i in range(N - 1):
        for j in range(i + 1, N):
            if List[j] < List[i]:
                List[i], List[j] = List[j], List[i]
    return List

L = [1, 2, 5, 3, 6, 8, 7]
print(bubble_sort(L))