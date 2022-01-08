def merge_two_sorted_arrays(arr1, arr2):
    l1, l2 = len(arr1), len(arr2)
    for i in range(l2 - 1, -1, -1):
        lst = arr1[-1]
        j = l1 - 2
        while j >= 0 and arr1[j] > arr2[i]:
            arr1[j + 1] = arr1[j]
            j -= 1
        if j != l1 - 2 or lst > arr2[i]:
            arr1[j + 1] = arr2[i]
            arr2[i] = lst

L1 = [1, 2, 4, 7, 9]
L2 = [0, 3, 5, 6, 8]
merge_two_sorted_arrays(L1, L2)
print(L1 + L2)