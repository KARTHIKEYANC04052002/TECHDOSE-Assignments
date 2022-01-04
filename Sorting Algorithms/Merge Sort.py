def merge_sort(List):
    if len(List) > 1:
        Mid = len(List) // 2
        L = List[:Mid]
        R = List[Mid:]
        merge_sort(L)
        merge_sort(R)
        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                List[k] = L[i]
                i += 1
            else:
                List[k] = R[j]
                j += 1
            k += 1
        while i < len(L):
            List[k] = L[i]
            i += 1
            k += 1
        while j < len(R):
            List[k] = R[j]
            j += 1
            k += 1
L = [5, 4, 6, 3, 1, 2]
merge_sort(L)
print(L)