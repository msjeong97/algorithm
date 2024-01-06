class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        numRows = len(grid)
        numColumns = len(grid[0])

        table = [[0 for c in range(numColumns)] for r in range(numRows)]
        table[0][0] = grid[0][0]

        for i in range(numRows):
            for j in range(numColumns):
                if i > 0 and j > 0:
                    table[i][j] = grid[i][j] + min(table[i - 1][j], table[i][j - 1])
                elif i > 0:
                    table[i][j] = grid[i][j] + table[i - 1][j]
                elif j > 0:
                    table[i][j] = grid[i][j] + table[i][j - 1]
                else:
                    continue
        
        return table[numRows - 1][numColumns - 1]
