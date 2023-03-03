# Given an integer array nums, find the subarray with the largest sum, and 
# return its sum. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
#  
# 
#  Example 3: 
# 
#  
# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  
# 
#  
#  Follow up: If you have figured out the O(n) solution, try coding another 
# solution using the divide and conquer approach, which is more subtle. 
# 
#  Related Topics Array Divide and Conquer Dynamic Programming 👍 28378 👎 1252
import math


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        result = -math.inf
        Sum = 0
        for num in nums:
            Sum += num
            result = max(result, Sum)
            if Sum < 0:
                Sum = 0
        return result
# leetcode submit region end(Prohibit modification and deletion)
