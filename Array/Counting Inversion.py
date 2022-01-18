def merge(L, temp, left, mid, right):
    i, j, k, inv_count = left, mid + 1, left, 0
    while i <= mid and j <= right:
        if L[i] <= L[j]:
            temp[k] = L[i]
            k += 1
            i += 1
        else:
            temp[k] = L[j]
            inv_count += mid - i + 1
            k += 1
            j += 1
    while i <= mid:
        temp[k] = L[i]
        k += 1
        i += 1
    while j <= right:
        temp[k] = L[i]
        k += 1
        j += 1
    for i in range(left, right + 1):
        L[i] = temp[i]
    return inv_count
    
def mergeSort(L, temp, left, right):
    inv_count = 0
    if left < right:
        mid = (left + right) // 2
        inv_count += mergeSort(L, temp, left, mid)
        inv_count += mergeSort(L, temp, mid+1, right)
        inv_count += merge(L, temp, left, mid, right)
    return inv_count

def countInversions(L):
    N = len(L)
    temp = [0] * N
    return mergeSort(L, temp, 0, N-1)

L = list(map(int, input().split()))
print(countInversions(L))