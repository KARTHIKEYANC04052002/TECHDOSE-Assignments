def twoSum(self, nums: List[int], target: int) -> List[int]:
	map_ = {}
	for i in range(len(nums)):
		X = nums[i]
		Y = target - X
		if Y in map_:
			return [i, map_[Y]]
		map_[X] = i