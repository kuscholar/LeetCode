from typing import List
import collections
import itertools
import functools
import math
import string
import random
import bisect
import re
import operator
import heapq
import queue

from queue import PriorityQueue
from itertools import combinations, permutations
from functools import lru_cache
from collections import defaultdict
from collections import OrderedDict
from collections import deque
from collections import Counter

# You are given an m x n integer array grid. There is a robot initially located 
# at the top-left corner (i.e., grid[0][0]). The robot tries to move to the 
# bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down 
# or right at any point in time. 
# 
#  An obstacle and space are marked as 1 or 0 respectively in grid. A path that 
# the robot takes cannot include any square that is an obstacle. 
# 
#  Return the number of possible unique paths that the robot can take to reach 
# the bottom-right corner. 
# 
#  The testcases are generated so that the answer will be less than or equal to 
# 2 * 10⁹. 
# 
#  
#  Example 1: 
#  
#  
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#  
# 
#  Example 2: 
#  
#  
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  m == obstacleGrid.length 
#  n == obstacleGrid[i].length 
#  1 <= m, n <= 100 
#  obstacleGrid[i][j] is 0 or 1. 
#  
# 
#  Related Topics Array Dynamic Programming Matrix 👍 6694 👎 431


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        # 1. dp array: ways to reach current position, index: number of unique ways to reach dp[i][j]
        # 2. function: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 3. init: dp[[0]*n]*m --> all is 0 at first, except dp[0][0]=1, because it's possible that obstacle blocks ways
        # 4. order: left to right, top to down
        # 5. eg: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]], [[1,1,1],[1,0,1],[1,1,2]]
        if obstacleGrid[-1][-1] == 1 or obstacleGrid[0][0] == 1:
            return 0
        dp = [[0]*len(obstacleGrid[0])]*len(obstacleGrid)
        dp[0][0] = 1
        for row in range(len(obstacleGrid)):
            for col in range(len(obstacleGrid[0])):
                if row == col == 0:
                    continue
                if obstacleGrid[row][col] == 1:
                    dp[row][col] = 0
                    continue
                if self.isValid(obstacleGrid, row-1, col):
                    top = dp[row-1][col]
                else:
                    top = 0
                if self.isValid(obstacleGrid, row, col-1):
                    left = dp[row][col-1]
                else:
                    left = 0
                dp[row][col] = top + left
        return dp[-1][-1]
    def isValid(self, obstacleGrid, row, col):
        return 0 <= row < len(obstacleGrid) and 0 <= col < len(obstacleGrid[0]) and obstacleGrid[row][col] == 0

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))