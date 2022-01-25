class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        N, hash_ = len(nums2), {}
        def getNext(start, val):
            for j in range(start, N):
                if nums2[j] > val:
                    return nums2[j]
            return -1
        for i in range(N):
            hash_[nums2[i]] = i
        return [getNext(hash_[i] + 1, i) for i in nums1]