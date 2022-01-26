class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [-1]
        heights += [0]
        top = -1
        area = 0
        for x, y in enumerate(heights):
            while heights[stack[top]] > y:
                h = heights[stack.pop()]
                w = x - stack[top] - 1
                area = max(area, h * w)
            stack += [x]
        return area