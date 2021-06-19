class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows = len(grid) 
        cols = len(grid[0])
        
        for row in range(rows):
            for col in range(cols):
          
                if row == 0 and col == 0:
                    continue
                if row == 0 or col == 0:
                    grid[row][col] += grid[row][col-1] if row == 0 else grid[row-1][col]
                else:
                    grid[row][col] += min(grid[row-1][col], grid[row][col-1])
                    
        return grid[-1][-1]
        