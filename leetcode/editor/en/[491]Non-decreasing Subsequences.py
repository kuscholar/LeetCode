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

# Given an integer array nums, return all the different possible non-decreasing 
# subsequences of the given array with at least two elements. You may return the 
# answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,6,7,7]
# Output: [[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [4,4,3,2,1]
# Output: [[4,4]]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 15 
#  -100 <= nums[i] <= 100 
#  
# 
#  Related Topics Array Hash Table Backtracking Bit Manipulation 👍 3274 👎 214


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        self.backtracking(nums, 0)
        return self.result

    def backtracking(self, nums, index):
        if len(self.path) >= 2:
            self.result.append(self.path[:])
        used = set()
        for i in range(index, len(nums)):
            if nums[i] in used:
                continue
            if i > index and nums[i] == nums[i-1]:
                continue
            if self.path and nums[i] < self.path[-1]:
                continue
            self.path.append(nums[i])
            used.add(nums[i])
            self.backtracking(nums, i+1)
            self.path.pop()

# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))