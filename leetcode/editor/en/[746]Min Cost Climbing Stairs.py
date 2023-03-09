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

# You are given an integer array cost where cost[i] is the cost of iᵗʰ step on 
# a staircase. Once you pay the cost, you can either climb one or two steps. 
# 
#  You can either start from the step with index 0, or the step with index 1. 
# 
#  Return the minimum cost to reach the top of the floor. 
# 
#  
#  Example 1: 
# 
#  
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
#  
# 
#  Example 2: 
# 
#  
# Input: cost = [1,100,1,1,1,100,1,1,100,1]
# Output: 6
# Explanation: You will start at index 0.
# - Pay 1 and climb two steps to reach index 2.
# - Pay 1 and climb two steps to reach index 4.
# - Pay 1 and climb two steps to reach index 6.
# - Pay 1 and climb one step to reach index 7.
# - Pay 1 and climb two steps to reach index 9.
# - Pay 1 and climb one step to reach the top.
# The total cost is 6.
#  
# 
#  
#  Constraints: 
# 
#  
#  2 <= cost.length <= 1000 
#  0 <= cost[i] <= 999 
#  
# 
#  Related Topics Array Dynamic Programming 👍 8979 👎 1404


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # 1. dp array: cost to reach top, index: min cost to reach ith floor
        # 2. function: dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        # 3. init: dp[0] = cost[0], dp[1] = cost[1]
        # 4. order: left to right
        # 5. eg: [1,100,1,1,1,100,1,1,100,1]: 1, 100, 2, 3, 3, 103, 4, 5, 104, 6
        if len(cost) <= 2:
            return min(cost)
        dp = [0] * len(cost)
        dp[0] = cost[0]
        dp[1] = cost[1]
        for i in range(len(cost)):
            dp[i] = min(dp[i-1], dp[i-2]) + cost[i]
        return min(dp[-1], dp[-2])

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))