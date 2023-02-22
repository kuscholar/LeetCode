# Given an array of positive integers nums and a positive integer target, 
# return the minimal length of a subarray whose sum is greater than or equal to target. 
# If there is no such subarray, return 0 instead. 
# 
#  
#  Example 1: 
# 
#  
# Input: target = 7, nums = [2,3,1,2,4,3]
# Output: 2
# Explanation: The subarray [4,3] has the minimal length under the problem 
# constraint.
#  
# 
#  Example 2: 
# 
#  
# Input: target = 4, nums = [1,4,4]
# Output: 1
#  
# 
#  Example 3: 
# 
#  
# Input: target = 11, nums = [1,1,1,1,1,1,1,1]
# Output: 0
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= target <= 10⁹ 
#  1 <= nums.length <= 10⁵ 
#  1 <= nums[i] <= 10⁴ 
#  
# 
#  
# Follow up: If you have figured out the 
# O(n) solution, try coding another solution of which the time complexity is 
# O(n log(n)).
# 
#  Related Topics Array Binary Search Sliding Window Prefix Sum 👍 8658 👎 241


# leetcode submit region begin(Prohibit modification and deletion)
import math


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if not target or not nums:
            return 0
        result = math.inf
        left, right = 0, 0
        currentSum = 0
        while right < len(nums):
            currentSum += nums[right]

            while currentSum >= target:
                if right - left + 1 < result:
                    result = right - left + 1
                currentSum -= nums[left]
                left += 1
            right += 1
        return result if result != math.inf else 0

# leetcode submit region end(Prohibit modification and deletion)
