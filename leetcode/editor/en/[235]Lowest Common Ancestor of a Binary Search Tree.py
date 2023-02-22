# Given a binary search tree (BST), find the lowest common ancestor (LCA) node 
# of two given nodes in the BST. 
# 
#  According to the definition of LCA on Wikipedia: “The lowest common ancestor 
# is defined between two nodes p and q as the lowest node in T that has both p 
# and q as descendants (where we allow a node to be a descendant of itself).” 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
# Output: 6
# Explanation: The LCA of nodes 2 and 8 is 6.
#  
# 
#  Example 2: 
#  
#  
# Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
# Output: 2
# Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant 
# of itself according to the LCA definition.
#  
# 
#  Example 3: 
# 
#  
# Input: root = [2,1], p = 2, q = 1
# Output: 2
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁵]. 
#  -10⁹ <= Node.val <= 10⁹ 
#  All Node.val are unique. 
#  p != q 
#  p and q will exist in the BST. 
#  
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 8872
#  👎 250


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # 1. parameter: root, p, q, return value: TreeNode
        # 2. ending: p < root.val < q or q < root.val < p
        # 3. each level: decide where to go
        if not root:
            return None
        if p.val <= root.val <= q.val or q.val <= root.val <= p.val:
            return root
        if root.val > max(p.val, q.val):
            return self.lowestCommonAncestor(root.left, p, q)
        if root.val < min(p.val, q.val):
            return self.lowestCommonAncestor(root.right, p, q)
        return None
# leetcode submit region end(Prohibit modification and deletion)
