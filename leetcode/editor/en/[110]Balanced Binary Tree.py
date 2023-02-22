# Given a binary tree, determine if it is height-balanced. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,3,3,null,null,4,4]
# Output: false
#  
# 
#  Example 3: 
# 
#  
# Input: root = []
# Output: true
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -10⁴ <= Node.val <= 10⁴ 
#  
# 
#  Related Topics Tree Depth-First Search Binary Tree 👍 8326 👎 471


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

"""
Time: O(n)
"""
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.getHeight(root) != -1
    def getHeight(self, root):
        if not root:
            return 0
        left = self.getHeight(root.left)
        if left == -1:
            return -1
        right = self.getHeight(root.right)
        if right == -1:
            return -1
        return -1 if abs(left - right) > 1 else 1 + max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
