# Given two integers n and k, return all possible combinations of k numbers 
# chosen from the range [1, n]. 
# 
#  You may return the answer in any order. 
# 
#  
#  Example 1: 
# 
#  
# Input: n = 4, k = 2
# Output: [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
# Explanation: There are 4 choose 2 = 6 total combinations.
# Note that combinations are unordered, i.e., [1,2] and [2,1] are considered to 
# be the same combination.
#  
# 
#  Example 2: 
# 
#  
# Input: n = 1, k = 1
# Output: [[1]]
# Explanation: There is 1 choose 1 = 1 total combination.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= n <= 20 
#  1 <= k <= n 
#  
# 
#  Related Topics Backtracking 👍 5737 👎 176


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        # we can have either global variables or pass them in the backtracking func
        self.path = []
        self.result = []
    def combine(self, n: int, k: int) -> List[List[int]]:
        if not k or not n:
            return []
        self.backtracking(n, k, 1)
        return self.result

    def backtracking(self, n, k, startIndex):
        # 1. parameters: n, k, startIndex, return: None
        # 2. ending: len(path) == k
        # 3. each level, use for loop to traverse
        if len(self.path) == k:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, n+1):
            self.path.append(i)
            self.backtracking(n, k, i+1)
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
