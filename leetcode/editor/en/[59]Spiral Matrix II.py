# Given a positive integer n, generate an n x n matrix filled with elements 
# from 1 to n² in spiral order. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3
# Output: [[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: [[1]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  
# 
#  Related Topics Array Matrix Simulation 👍 4571 👎 203


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        if not n:
            return [[]]
        result = [[0] * n for _ in range(n)]
        startRow, startCol = 0, 0
        count = 1
        for level in range(n//2):
            for i in range(startCol, n-level-1):
                result[startRow][i] = count
                count += 1
            for i in range(startRow, n-level-1):
                result[i][n-level-1] = count
                count += 1
            for i in range(n-level-1, startCol, -1):
                result[n-level-1][i] = count
                count += 1
            for i in range(n-level-1, startRow, -1):
                result[i][startCol] = count
                count += 1
            startCol += 1
            startRow += 1

        if n%2 != 0:
            result[startRow][startCol] = n*n
        return result
# leetcode submit region end(Prohibit modification and deletion)
