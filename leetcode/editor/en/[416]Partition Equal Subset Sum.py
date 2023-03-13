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

# Given an integer array nums, return true if you can partition the array into 
# two subsets such that the sum of the elements in both subsets is equal or false 
# otherwise. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,5,11,5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1,2,3,5]
# Output: false
# Explanation: The array cannot be partitioned into equal sum subsets.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 200 
#  1 <= nums[i] <= 100 
#  
# 
#  Related Topics Array Dynamic Programming 👍 10031 👎 176


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        
# leetcode submit region end(Prohibit modification and deletion)


if __name__ == "__main__":
    # test = []
    # print(Solution().function(test))