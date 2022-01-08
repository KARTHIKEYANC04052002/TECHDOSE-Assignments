def maximumGap(self, nums: List[int]) -> int:
    Max_diff = 0
    nums.sort()
    for i in range(1, len(nums)):
        if nums[i] - nums[i - 1] > Max_diff:
            Max_diff = nums[i] - nums[i - 1]
    return Max_diff