class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        n = len(grid)
        m = len(grid[0])
        seen = [[False] * m for _ in range(n)]
        max_area = 0

        def dfs (row, col):
            seen[row][col] = True
            area = 1
            for direc in directions:
                nr = row + direc[0]
                nc = col + direc[1]
                if (isValid(nr, nc) and not seen[nr][nc]):
                    area +=  dfs(nr, nc)
            return area
        
        def isValid (row, col):
            return 0 <= row < n and 0 <= col < m and grid[row][col] == 1

        for i in range (n):
            for j in range (m):
                if grid[i][j] == 1 and not seen[i][j]:
                    max_area = max(max_area, dfs(i, j))
        
        return max_area