def partition(List, start, end):
    piv_ind = start
    piv = List[piv_ind]
    while start < end:
        while start < len(List) and List[start] <= piv:
            start += 1
        while List[end] > piv:
            end -= 1
        if start < end:
            List[start], List[end] = List[end], List[start]
    List[end], List[piv_ind] = List[piv_ind], List[end]
    return end
def quick_sort(List, start, end):
    if start < end:
        p = partition(List, start, end)
        quick_sort(List, start, p - 1)
        quick_sort(List, p + 1, end)
L = [5, 4, 6, 3, 1, 2]
quick_sort(L, 0, len(L) - 1)
print(L)