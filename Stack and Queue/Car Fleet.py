class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        N = len(position)
        stack = []
        for pos, spe in sorted(zip(position, speed),reverse = True):
            time = (target - pos) / spe
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)