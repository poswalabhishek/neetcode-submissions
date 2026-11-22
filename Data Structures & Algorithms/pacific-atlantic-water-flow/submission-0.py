class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # lets go from ocean to all the possible cells

        n = len(heights)
        m = len(heights[0])
        atlantic_set = set()
        pacific_set = set()

        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def isValid (row, col):
            return 0 <= row < n and 0 <= col < m

        def dfs (row, col, visit_set, prev_height):
            if (not isValid(row, col) or (row, col) in visit_set or prev_height > heights[row][col]):
                return
            
            visit_set.add((row, col))
            
            for direc in directions:
                nr = direc[0] + row
                nc = direc[1] + col
                if (isValid(nr, nc)):
                    dfs (nr, nc, visit_set, heights[row][col])
            


        # left and right cols
        for col in range (m):
            dfs (0, col, pacific_set, heights[0][col])
            dfs (n - 1, col, atlantic_set, heights[n - 1][col])
        
        # top and bottom rows
        for row in range (n):
            dfs (row, 0, pacific_set, heights[row][0])
            dfs (row, m - 1, atlantic_set, heights[row][m - 1])

        res = []
        for r in range(n):
            for c in range(m):
                if (r, c) in pacific_set and (r, c) in atlantic_set:
                    res.append([r, c])
        return res