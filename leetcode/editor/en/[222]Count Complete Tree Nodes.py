# Given the root of a complete binary tree, return the number of the nodes in 
# the tree. 
# 
#  According to Wikipedia, every level, except possibly the last, is completely 
# filled in a complete binary tree, and all nodes in the last level are as far 
# left as possible. It can have between 1 and 2ʰ nodes inclusive at the last level h.
#  
# 
#  Design an algorithm that runs in less than O(n) time complexity. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,2,3,4,5,6]
# Output: 6
#  
# 
#  Example 2: 
# 
#  
# Input: root = []
# Output: 0
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5 * 10⁴]. 
#  0 <= Node.val <= 5 * 10⁴ 
#  The tree is guaranteed to be complete. 
#  
# 
#  Related Topics Binary Search Tree Depth-First Search Binary Tree 👍 7116 👎 3
# 96


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1
# leetcode submit region end(Prohibit modification and deletion)
