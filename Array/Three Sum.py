def twoSums(self, num, res, i):
    st = i + 1
    en = len(num) - 1
    while st < en:
        sum_ = num[i] + num[st] + num[en]
        if sum_ < 0:
            st += 1
        elif sum_ > 0:
            en -= 1
        else:
            res.append([num[i], num[st], num[en]])
            st += 1
            en -= 1
            while st < en and num[st] == num[st - 1]:
                st += 1

def threeSum(self, nums: List[int]) -> List[List[int]]:
    N, res = len(nums), []
    nums.sort()
    for i in range(N):
        if nums[i] > 0:
            break
        if i == 0 or nums[i - 1] != nums[i]:
            self.twoSums(nums, res, i)
    return res