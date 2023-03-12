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

# Given an integer n, break it into the sum of k positive integers, where k >= 2
# , and maximize the product of those integers. 
# 
#  Return the maximum product you can get. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 2
# Output: 1
# Explanation: 2 = 1 + 1, 1 × 1 = 1.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 10
# Output: 36
# Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= n <= 58 
#  
# 
#  Related Topics Math Dynamic Programming 👍 3548 👎 360


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def integerBreak(self, n: int) -> int:
        # 1. dp array: max product, index: max product at number i
        # 2. function: dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        # 3. init: dp[0]*(n+1), dp[2] = 1
        # 4. order: left to right
        # 5. eg: [0,0,1,2,4,6,9]
        dp = [0]*(n+1)
        dp[2] = 1
        for i in range(3, n+1):
            for j in range(1, i//2+1):
                dp[i] = max(dp[i], max(j*(i-j), j*dp[i-j]))
        return dp[n]

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))