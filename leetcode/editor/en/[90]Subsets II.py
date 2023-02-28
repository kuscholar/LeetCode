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

# Given an integer array nums that may contain duplicates, return all possible 
# subsets (the power set). 
# 
#  The solution set must not contain duplicate subsets. Return the solution in 
# any order. 
# 
#  
#  Example 1: 
#  Input: nums = [1,2,2]
# Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
#  Example 2: 
#  Input: nums = [0]
# Output: [[],[0]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
# 
#  Related Topics Array Backtracking Bit Manipulation 👍 7633 👎 218


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        # 1. parameter: nums, index; return: None
        # 2. ending: every step append
        # 3. each level: remove duplicate
        if not nums:
            return []
        nums.sort()
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, index):
        self.result.append(self.path[:])
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i-1]:
                continue
            self.path.append(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))