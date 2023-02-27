# Given a string s, partition s such that every substring of the partition is a 
# palindrome. Return all possible palindrome partitioning of s. 
# 
#  
#  Example 1: 
#  Input: s = "aab"
# Output: [["a","a","b"],["aa","b"]]
#  
#  Example 2: 
#  Input: s = "a"
# Output: [["a"]]
#  
#  
#  Constraints: 
# 
#  
#  1 <= s.length <= 16 
#  s contains only lowercase English letters. 
#  
# 
#  Related Topics String Dynamic Programming Backtracking 👍 10247 👎 325

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

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []

    def partition(self, s: str) -> List[List[str]]:
        # 1. parameters: s, startIndex, return: None
        # 2. ending: startIndex >= len(s)
        # 3. each level: determine if so far path is palindrome
        if not s:
            return []
        self.backtracking(list(s), 0)
        return self.result

    def backtracking(self, s, startIndex):
        if startIndex >= len(s):
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(s)):
            if self.isPalindrome(s[startIndex:i+1]):
                self.path.append(''.join(s[startIndex:i+1]))
            else:
                continue
            # if the program reaches here, it means path already added previous substring
            self.backtracking(s, i+1)
            self.path.pop()

    def isPalindrome(self, subString):
        return subString == subString[::-1]

if __name__ == "__main__":
    test = "aab"
    print(Solution().partition(test))
# leetcode submit region end(Prohibit modification and deletion)
