class Solution:
    def countIslands(self, grid: list[list[int]], k: int) -> int:
        if not grid or not grid[0]:
            return 0
            
        m, n = len(grid), len(grid[0])
        divisible_islands_count = 0

        def dfs(r: int, c: int) -> int:
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] <= 0:
                return 0
            
            total_remainder = grid[r][c] % k
            grid[r][c] = -1 # Mark as visited in-place
            
            total_remainder = (total_remainder + dfs(r - 1, c)) % k # Up
            total_remainder = (total_remainder + dfs(r + 1, c)) % k # Down
            total_remainder = (total_remainder + dfs(r, c - 1)) % k # Left
            total_remainder = (total_remainder + dfs(r, c + 1)) % k # Right
            
            return total_remainder

        for r in range(m):
            for c in range(n):
                if grid[r][c] > 0:
                    if dfs(r, c) == 0:
                        divisible_islands_count += 1
                        
        return divisible_islands_count