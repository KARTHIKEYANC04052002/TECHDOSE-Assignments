class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N, hash_ = len(nums2), {}
        def getPrev(end, val):
            for j in range(end-1, -1, -1):
                if nums2[j] < val:
                    return nums2[j]
            return -1
        for i in range(N):
            hash_[nums2[i]] = i
        return [getPrev(hash_[i] + 1, i) for i in nums1]