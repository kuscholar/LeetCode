# Given an integer array nums where the elements are sorted in ascending order, 
# convert it to a height-balanced binary search tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: nums = [-10,-3,0,5,9]
# Output: [0,-3,9,-10,null,5]
# Explanation: [0,-10,5,null,-3,null,9] is also accepted:
# 
#  
# 
#  Example 2: 
#  
#  
# Input: nums = [1,3]
# Output: [3,1]
# Explanation: [1,null,3] and [3,1] are both height-balanced BSTs.
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums is sorted in a strictly increasing order. 
#  
# 
#  Related Topics Array Divide and Conquer Tree Binary Search Tree Binary Tree ?
# ? 9100 👎 459


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        return self.traverse(nums, 0, len(nums)-1)
    def traverse(self, nums, left, right):
        # 1. parameter: nums, left, right, return: TreeNode
        # 2. ending: left > right
        # 3. each level: construct
        if left > right:
            return None
        mid = (left + right) // 2
        root = TreeNode(nums[mid])
        root.left = self.traverse(nums, left, mid-1)
        root.right = self.traverse(nums, mid+1, right)
        return root


# leetcode submit region end(Prohibit modification and deletion)
