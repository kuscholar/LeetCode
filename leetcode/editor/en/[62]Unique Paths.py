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

# There is a robot on an m x n grid. The robot is initially located at the top-
# left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right 
# corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at 
# any point in time. 
# 
#  Given the two integers m and n, return the number of possible unique paths 
# that the robot can take to reach the bottom-right corner. 
# 
#  The test cases are generated so that the answer will be less than or equal 
# to 2 * 10⁹. 
# 
#  
#  Example 1: 
#  
#  
# Input: m = 3, n = 7
# Output: 28
#  
# 
#  Example 2: 
# 
#  
# Input: m = 3, n = 2
# Output: 3
# Explanation: From the top-left corner, there are a total of 3 ways to reach 
# the bottom-right corner:
# 1. Right -> Down -> Down
# 2. Down -> Down -> Right
# 3. Down -> Right -> Down
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= m, n <= 100 
#  
# 
#  Related Topics Math Dynamic Programming Combinatorics 👍 13209 👎 377


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 1. dp array: ways to reach current position, index: number of unique ways to reach dp[i][j]
        # 2. function: dp[i][j] = dp[i-1][j] + dp[i][j-1]
        # 3. init: dp[[1]*n]*m --> all is 1 at first
        # 4. order: left to right, top to down
        # 5. eg: m = 3, n = 2, [[0, 1],[1, 2],[1, 3]]
        self.m = m
        self.n = n
        dp = [[1]*n]*m
        for row in range(1, m):
            for col in range(1, n):
                if self.isValid(row-1, col):
                    top = dp[row-1][col]
                else:
                    top = 0
                if self.isValid(row, col-1):
                    left = dp[row][col-1]
                else:
                    left = 0
                dp[row][col] = top + left
        return dp[-1][-1]

    def isValid(self, row, col):
        return 0 <= row < self.m and 0 <= col < self.n
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))