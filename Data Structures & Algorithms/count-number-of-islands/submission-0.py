class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        seen = [[False] * m for _ in range(n)]
    
        def isValid (row, col) -> bool:
            return 0 <= row and 0 <= col and row < n and col < m and grid[row][col] == "1"
        
        def dfs (row, col):
            for direc in directions:
                new_row = direc[0] + row
                new_col = direc[1] + col
                if (isValid(new_row, new_col) and not seen[new_row][new_col]):
                    seen[new_row][new_col] = True
                    dfs(new_row, new_col)
        
        island_count = 0
        for i in range (n):
            for j in range (m):
                if grid[i][j] == "1" and not seen[i][j]:
                    dfs(i, j)
                    island_count += 1
        
        return island_count

# grid = [
#     ["0","1","1","1","0"],
#     ["0","1","0","1","0"],
#     ["1","1","0","0","0"],
#     ["0","0","0","0","0"]
#   ]


