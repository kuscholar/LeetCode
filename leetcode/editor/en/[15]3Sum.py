# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[
# k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0. 
# 
#  Notice that the solution set must not contain duplicate triplets. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not 
# matter.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
#  
# 
#  
#  Constraints: 
# 
#  
#  3 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
# 
#  Related Topics Array Two Pointers Sorting 👍 23954 👎 2186

"""
After sort: [-4,-1,-1,0,1,2]
"""

# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if not nums or len(nums) < 3:
            return result
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                Set = [nums[i], nums[left], nums[right]]
                if sum(Set) < 0:
                    left += 1
                elif sum(Set) > 0:
                    right -= 1
                else:
                    result.append(Set)

                    # NOTE: only remove duplicate after finding the solution here
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return result

# leetcode submit region end(Prohibit modification and deletion)
