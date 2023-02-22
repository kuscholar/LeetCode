# Given a binary tree, find its minimum depth. 
# 
#  The minimum depth is the number of nodes along the shortest path from the 
# root node down to the nearest leaf node. 
# 
#  Note: A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [3,9,20,null,null,15,7]
# Output: 2
#  
# 
#  Example 2: 
# 
#  
# Input: root = [2,null,3,null,4,null,5,null,6]
# Output: 5
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 10⁵]. 
#  -1000 <= Node.val <= 1000 
#  
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Tree 👍 53
# 78 👎 1078


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        Min = math.inf
        if root.left:
            Min = min(self.minDepth(root.left), Min)
        if root.right:
            Min = min(self.minDepth(root.right), Min)
        return 1 + Min
# leetcode submit region end(Prohibit modification and deletion)
