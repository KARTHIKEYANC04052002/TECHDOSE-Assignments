class Solution:
    def minAbsDifference(self, nums: List[int], goal: int) -> int:
        part1, part2, parts_sum = nums[::2], nums[1::2], [{0}, {0}]
        for i, numbers in enumerate([part1, part2]):
            for num in numbers:
                parts_sum[i] |= {num + s for s in parts_sum[i]}
        part1_sum, part2_sum = parts_sum
        part2_sum = sorted(part2_sum)
        result = 10 ** 10
        for num in part1_sum:
            target = goal - num
            if (part2_sum[0] - result) < target < (part2_sum[-1] + result):
                index = bisect_left(part2_sum, target)
                for i in [index-1, index]:
                    if 0 <= i < len(part2_sum):
                        result = min(result, abs(target - part2_sum[i]))
                        if result == 0:
                            return 0
        return result