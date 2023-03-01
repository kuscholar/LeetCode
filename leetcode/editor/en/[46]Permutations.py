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

# Given an array nums of distinct integers, return all the possible 
# permutations. You can return the answer in any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#  
#  Example 2: 
#  Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#  
#  Example 3: 
#  Input: nums = [1]
# Output: [[1]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 6 
#  -10 <= nums[i] <= 10 
#  All the integers of nums are unique. 
#  
# 
#  Related Topics Array Backtracking 👍 14850 👎 253


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1. parameters: nums, used; return: None
        # 2. ending: len(self.path) == len(nums)
        # 3. each level: traverse
        if not nums:
            return []
        self.backtracking(nums, [False]*len(nums))
        return self.result

    def backtracking(self, nums, used):
        if len(self.path) == len(nums):
            self.result.append(self.path[:])
            return
        for i in range(len(nums)):
            if used[i] == True:
                continue
            self.path.append(nums[i])
            used[i] = True
            self.backtracking(nums, used)
            used[i] = False
            self.path.pop()

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))