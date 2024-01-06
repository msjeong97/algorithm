class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        numRows = len(obstacleGrid)
        numColumns = len(obstacleGrid[0])

        resultTable = [[0 for c in range(numColumns)] for r in range(numRows)]
        resultTable[0][0] = 1

        for i in range(numRows):
            for j in range(numColumns):
                if obstacleGrid[i][j] == 1:
                    resultTable[i][j] = 0
                    continue

                if i > 0:
                   resultTable[i][j] = resultTable[i][j] + resultTable[i - 1][j] 
                if j > 0:
                    resultTable[i][j] = resultTable[i][j] + resultTable[i][j - 1] 

        return resultTable[numRows - 1][numColumns - 1]
