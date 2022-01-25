class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        insort(self.nums, num)

    def findMedian(self) -> float:
        length = len(self.nums)
        if length == 0:
            return None
        mid = length // 2
        if length & 1:
            return self.nums[mid]
        return (self.nums[mid] + self.nums[mid-1]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()