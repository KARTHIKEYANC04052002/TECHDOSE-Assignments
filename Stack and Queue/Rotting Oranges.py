from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        orange_count = rot_orange_count = 0
        R, C = len(grid), len(grid[0])
        queue = deque()
        for i in range(R):
            for j in range(C):
                if grid[i][j] >= 1:
                    orange_count += 1
                if grid[i][j] == 2:
                    queue.appendleft((i, j))
                    rot_orange_count += 1
        if orange_count == 0:
            return 0
        lvl = -1
        visited_count = 0
        while queue:
            count, rot_orange_count = rot_orange_count, 0
            for i in range(count):
                row, col = queue.pop()
                visited_count += 1
                for x, y in ((row-1, col), (row, col-1), (row, col+1), (row+1, col)):
                    if x >= 0 and x < R and y >= 0 and y < C and grid[x][y] == 1:
                        grid[x][y] = 2
                        queue.appendleft((x, y))
                        rot_orange_count += 1
            lvl += 1
        if visited_count == orange_count:
            return lvl
        return -1