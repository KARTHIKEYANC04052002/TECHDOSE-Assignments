def singleNumber(self, nums: List[int]) -> int:
    N, count, neg_count = len(nums), [0] * 32, 0
    for i in range(N):
        X = nums[i]
        if X < 0:
            neg_count += 1
            X = -X
        for j in range(32):
            if X & (1<<j) != 0:
                count[j] += 1
    res = 0
    for i in range(32):
        res += count[i] % 3 * (1<<i)
    if neg_count % 3 != 0:
        res = -res
    return res