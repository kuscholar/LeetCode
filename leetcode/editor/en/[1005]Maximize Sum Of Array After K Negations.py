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

# Given an integer array nums and an integer k, modify the array in the 
# following way: 
# 
#  
#  choose an index i and replace nums[i] with -nums[i]. 
#  
# 
#  You should apply this process exactly k times. You may choose the same index 
# i multiple times. 
# 
#  Return the largest possible sum of the array after modifying it in this way. 
# 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [4,2,3], k = 1
# Output: 5
# Explanation: Choose index 1 and nums becomes [4,-2,3].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [3,-1,0,2], k = 3
# Output: 6
# Explanation: Choose indices (1, 2, 2) and nums becomes [3,1,0,2].
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [2,-3,-1,5,-4], k = 2
# Output: 13
# Explanation: Choose indices (1, 4) and nums becomes [2,3,-1,5,4].
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -100 <= nums[i] <= 100 
#  1 <= k <= 10⁴ 
#  
# 
#  Related Topics Array Greedy Sorting 👍 1276 👎 96


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        if not k:
            return sum(nums)
        nums.sort()
        for i, num in enumerate(nums):
            if num >= 0 or k == 0:
                break
            nums[i] = -num
            k -= 1
        if k == 0 or k % 2 == 0:
            return sum(nums)
        nums.sort()
        nums[0] = -nums[0]
        return sum(nums)
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))