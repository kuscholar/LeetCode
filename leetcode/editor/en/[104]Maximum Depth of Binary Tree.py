# Given the root of a binary tree, return its maximum depth. 
# 
#  A binary tree's maximum depth is the number of nodes along the longest path 
# from the root node down to the farthest leaf node. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 3
#  
# 
#  Example 2: 
# 
#  
# Input: root = [1,null,2]
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁴]. 
#  -100 <= Node.val <= 100 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 96
# 23 👎 156


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def largerDepth(root, depth):
            if not root:
                return depth
            left = largerDepth(root.left, depth+1)
            right = largerDepth(root.right, depth+1)
            return max(left, right)

        if not root:
            return 0
        left = largerDepth(root.left,1)
        right = largerDepth(root.right,1)
        return max(left, right)
# leetcode submit region end(Prohibit modification and deletion)
