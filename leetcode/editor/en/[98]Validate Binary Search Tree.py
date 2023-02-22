# Given the root of a binary tree, determine if it is a valid binary search 
# tree (BST). 
# 
#  A valid BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than the 
# node's key. 
#  The right subtree of a node contains only nodes with keys greater than the 
# node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [2,1,3]
# Output: true
#  
# 
#  Example 2: 
#  
#  
# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -2³¹ <= Node.val <= 2³¹ - 1 
#  
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 1392
# 6 👎 1149


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import math


class Solution:
    def __init__(self):
        # self.maxVal = -float("INF")
        self.maxVal = -math.inf

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # 1. parameter: root, return value: bool
        # 2. ending: leaf node/None?
        # 3. each level: left/right val
        if not root:
            return True
        left = self.isValidBST(root.left)
        if root.val > self.maxVal:
            self.maxVal = root.val
        else:
            return False
        right = self.isValidBST(root.right)
        return left and right

# leetcode submit region end(Prohibit modification and deletion)
