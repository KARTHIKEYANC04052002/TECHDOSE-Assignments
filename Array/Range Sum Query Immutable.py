class NumArray:

    def __init__(self, nums: List[int]):
        self.rangeSum = [0]
        for i in range(len(nums)):
            self.rangeSum += [self.rangeSum[-1] + nums[i]]

    def sumRange(self, left: int, right: int) -> int:
        return self.rangeSum[right + 1] - self.rangeSum[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)