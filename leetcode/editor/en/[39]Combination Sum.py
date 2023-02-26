# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the chosen numbers 
# sum to target. You may return the combinations in any order. 
# 
#  The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen 
# numbers is different. 
# 
#  The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input. 
# 
#  
#  Example 1: 
# 
#  
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple 
# times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#  
# 
#  Example 2: 
# 
#  
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#  
# 
#  Example 3: 
# 
#  
# Input: candidates = [2], target = 1
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= candidates.length <= 30 
#  2 <= candidates[i] <= 40 
#  All elements of candidates are distinct. 
#  1 <= target <= 40 
#  
# 
#  Related Topics Array Backtracking 👍 15173 👎 302


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def __init__(self):
        self.path = []
        self.result = []
        self.sum = 0
        self.set = set()
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 1. parameters: candidates, target, return: None
        # 2. ending: self.sum > target
        # 3. each level: traverse
        if not candidates:
            return []
        self.backtracking(candidates, target)
        return self.result

    def backtracking(self, candidates, target):
        if self.sum == target:
            if self.path[:].sort() not in self.set:
                self.result.append(self.path[:])
                self.set.add(self.path[:].sort())
            return
        if self.sum > target:
            return
        print(self.path)
        for candidate in candidates:
            self.path.append(candidate)
            self.sum += candidate
            self.backtracking(candidates, target)
            self.sum -= candidate
            self.path.pop()

# leetcode submit region end(Prohibit modification and deletion)
