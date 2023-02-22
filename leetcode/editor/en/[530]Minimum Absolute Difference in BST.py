# Given the root of a Binary Search Tree (BST), return the minimum absolute 
# difference between the values of any two different nodes in the tree. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [4,2,6,1,3]
# Output: 1
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,0,48,null,null,12,49]
# Output: 1
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [2, 10⁴]. 
#  0 <= Node.val <= 10⁵ 
#  
# 
#  
#  Note: This question is the same as 783: https://leetcode.com/problems/
# minimum-distance-between-bst-nodes/ 
# 
#  Related Topics Tree Depth-First Search Breadth-First Search Binary Search 
# Tree Binary Tree 👍 2747 👎 144


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        # 1. parameter: root, return value: None
        # 2. ending: no child nodes
        # 3. each level: calculate diff
        if not root:
            return 0
        self.minDiff = math.inf
        self.pre = None
        def traverse(cur):
            if not cur:
                return
            traverse(cur.left)
            if self.pre and abs(self.pre.val-cur.val) < self.minDiff:
                self.minDiff = abs(self.pre.val-cur.val)
            self.pre = cur
            traverse(cur.right)
        traverse(root)
        return self.minDiff
# leetcode submit region end(Prohibit modification and deletion)
