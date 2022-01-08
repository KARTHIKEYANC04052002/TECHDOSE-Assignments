def largest_sum_contiguous_subarray(arr):

    max_so_far = arr[0]
    max_ending_here = 0
    
    for i in range(len(arr)):
        max_ending_here = max_ending_here + arr[i]
        if max_ending_here < 0:
            max_ending_here = 0
        elif max_so_far < max_ending_here:
            max_so_far = max_ending_here
        print(i, arr[i], max_so_far)
    return max_so_far

L = [1, 2, -2, 4, -3, 3, 6, -5, 2, 1]
print(largest_sum_contiguous_subarray(L))