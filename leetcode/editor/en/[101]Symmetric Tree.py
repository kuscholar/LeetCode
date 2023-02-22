# Given the root of a binary tree, check whether it is a mirror of itself (i.e.,
#  symmetric around its center). 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,2,3,4,4,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,2,null,3,null,3]
# Output: false
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 1000]. 
#  -100 <= Node.val <= 100 
#  
# 
#  
# Follow up: Could you solve it both recursively and iteratively?
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 12
# 217 👎 275


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.compare(root.left, root.right)

    def compare(self, left, right):
        if not left and not right:
            return True
        elif not left:
            return False
        elif not right:
            return False
        # this left and right are not the root.left and root.right! but passed in nodes
        elif left.val != right.val:
            return False
        outside = self.compare(left.left, right.right)
        inside = self.compare(left.right, right.left)
        return outside and inside
# leetcode submit region end(Prohibit modification and deletion)
