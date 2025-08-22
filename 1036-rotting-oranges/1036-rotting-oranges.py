class Solution(object):
    def orangesRotting(self, grid):
        rows, cols = len(grid), len(grid[0])
        queue = []  
        fresh = 0

       
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 2:
                    queue.append((r, c))  
                elif grid[r][c] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = -1
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        while queue:
            new_queue = []  
            for x, y in queue:
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < rows and 0 <= ny < cols and grid[nx][ny] == 1:
                        grid[nx][ny] = 2  
                        fresh -= 1
                        new_queue.append((nx, ny))
            queue = new_queue
            minutes += 1

        return minutes if fresh == 0 else -1
