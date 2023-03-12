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

# Given an integer n, return the number of structurally unique BST's (binary 
# search trees) which has exactly n nodes of unique values from 1 to n. 
# 
#  
#  Example 1: 
#  
#  
# Input: n = 3
# Output: 5
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 19 
#  
# 
#  Related Topics Math Dynamic Programming Tree Binary Search Tree Binary Tree ?
# ? 8875 👎 353


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numTrees(self, n: int) -> int:
        # 1. dp array: number of unique BST with n nodes, index: number of unique BST with i nodes
        # 2. function: dp[i] += dp[j-1] * dp[i-j]
        # 3. init: dp[0] = 1
        # 4. order: left to right
        # 5. eg: [1,1,2,5,14]
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            for j in range(1, i+1):
                dp[i] += dp[j-1] * dp[i-j]
        return dp[n]
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))