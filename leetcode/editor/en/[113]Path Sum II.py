# Given the root of a binary tree and an integer targetSum, return all root-to-
# leaf paths where the sum of the node values in the path equals targetSum. Each 
# path should be returned as a list of the node values, not node references. 
# 
#  A root-to-leaf path is a path starting from the root and ending at any leaf 
# node. A leaf is a node with no children. 
# 
#  
#  Example 1: 
#  
#  
# Input: root = [5,4,8,11,null,13,4,7,2,null,null,5,1], targetSum = 22
# Output: [[5,4,11,2],[5,8,4,5]]
# Explanation: There are two paths whose sum equals targetSum:
# 5 + 4 + 11 + 2 = 22
# 5 + 8 + 4 + 5 = 22
#  
# 
#  Example 2: 
#  
#  
# Input: root = [1,2,3], targetSum = 5
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: root = [1,2], targetSum = 0
# Output: []
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [0, 5000]. 
#  -1000 <= Node.val <= 1000 
#  -1000 <= targetSum <= 1000 
#  
# 
#  Related Topics Backtracking Tree Depth-First Search Binary Tree 👍 6735 👎 13
# 9


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        self.result = []
        self.traverse(root, targetSum-root.val, [root.val])
        return self.result

    def traverse(self, root, count, path):
        if not root.left and not root.right and count == 0:
            self.result.append(path[:])   # NOTE: cannot use .append(path), which will append a reference to path
            return
        if not root.left and not root.right and count != 0:
            return
        if root.left:
            count -= root.left.val
            path.append(root.left.val)
            self.traverse(root.left, count, path)
            count += root.left.val
            path.pop()
        if root.right:
            count -= root.right.val
            path.append(root.right.val)
            self.traverse(root.right, count, path)
            count += root.right.val
            path.pop()
        return
# leetcode submit region end(Prohibit modification and deletion)
