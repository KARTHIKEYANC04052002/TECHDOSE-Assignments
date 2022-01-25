class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        AB = {}
        for x in nums1:
            for y in nums2:
                AB[x + y] = AB.get(x+y, 0) + 1
        Ans = 0
        for x in nums3:
            for y in nums4:
                Ans = Ans + AB.get(-(x+y), 0)
        return Ans