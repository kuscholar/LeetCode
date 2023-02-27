# Given a collection of candidate numbers (candidates) and a target number (
# target), find all unique combinations in candidates where the candidate numbers sum 
# to target. 
# 
#  Each number in candidates may only be used once in the combination. 
# 
#  Note: The solution set must not contain duplicate combinations. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [10,1,2,7,6,1,5], target = 8
# Output: 
# [
# [1,1,6],
# [1,2,5],
# [1,7],
# [2,6]
# ]
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,5,2,1,2], target = 5
# Output: 
# [
# [1,2,2],
# [5]
# ]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 100 
#  1 <= candidates[i] <= 50 
#  1 <= target <= 30 
#  
# 
#  Related Topics Array Backtracking 👍 8008 👎 200


# leetcode submit region begin(Prohibit modification and deletion)

# class Solution:
#     def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
#         res = []
#         tmp = []
#         candidates.sort()
#         self.dfs(candidates, target, 0, res, tmp)
#         return res
#
#     def dfs(self, candidates, target, index, res, tmp):
#         if target < 0:
#             return
#         if target == 0:
#             res.append(list(tmp))
#             return
#         for i in range(index, len(candidates)):
#             if i > index and candidates[i] == candidates[i - 1]:
#                 continue
#             tmp.append(candidates[i])
#             self.dfs(candidates, target - candidates[i], i + 1, res, tmp)
#             tmp.pop()

class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.sum = 0

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. parameters: candidates, target, index, return: None
        # 2. ending: self.sum > target, or self.sum == target
        # 3. each level: traverse
        if not candidates:
            return []
        candidates.sort()
        self.backtracking(candidates, target, 0)
        return self.result

    def backtracking(self, candidates, target, startIndex):
        if self.sum > target:
            return
        if self.sum == target:
            self.result.append(self.path[:])
            return
        for i in range(startIndex, len(candidates)):
            # remove duplicate!!
            if i > startIndex and candidates[i] == candidates[i-1]:
                continue
            self.path.append(candidates[i])
            self.sum += candidates[i]
            self.backtracking(candidates, target, i+1)
            self.sum -= candidates[i]
            self.path.pop()
# leetcode submit region end(Prohibit modification and deletion)
