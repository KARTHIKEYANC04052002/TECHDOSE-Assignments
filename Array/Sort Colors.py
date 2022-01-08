def sortColors(self, nums: List[int]) -> None:
    C = [0 for i in range(3)]
    for i in nums:
        C[i] += 1
    X = 0
    L, i = len(nums), 0
    while i < L:
        if C[X] > 0:
            nums[i] = X
            C[X] -= 1
            i += 1
        else:
            X += 1
    return nums