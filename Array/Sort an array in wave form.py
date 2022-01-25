def sortArrWave(arr, N):
    for i in range(0, N, 2):
        if i > 0 and arr[i] < arr[i-1]:
            arr[i], arr[i-1] = arr[i-1], arr[i]
        if i < N - 1 and arr[i] < arr[i+1]:
            arr[i], arr[i+1] = arr[i+1], arr[i]

arr = [1, 2, 3, 4, 5, 6]
sortArrWave(arr, len(arr))
print(arr)