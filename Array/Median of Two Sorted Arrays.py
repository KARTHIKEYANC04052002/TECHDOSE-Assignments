def findMedianSortedArrays(self, L1: List[int], L2: List[int]) -> float:
    N, M = len(L1), len(L2)
    NM = N + M
    i, j, k, res = 0, 0, 0, [0] * (NM)
    while i < N and j < M:
        if L1[i] < L2[j]:
            res[k] = L1[i]
            i += 1
        else:
            res[k] = L2[j]
            j += 1
        k += 1
    while i < N:
        res[k] = L1[i];
        i += 1
        k += 1
    while j < M:
        res[k] = L2[j];
        j += 1
        k += 1
    if (NM) & 1:
        return res[NM // 2]
    return (res[NM // 2] + res[NM // 2 - 1]) / 2
