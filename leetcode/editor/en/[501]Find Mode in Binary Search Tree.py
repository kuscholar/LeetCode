# Given the root of a binary search tree (BST) with duplicates, return all the 
# mode(s) (i.e., the most frequently occurred element) in it. 
# 
#  If the tree has more than one mode, return them in any order. 
# 
#  Assume a BST is defined as follows: 
# 
#  
#  The left subtree of a node contains only nodes with keys less than or equal 
# to the node's key. 
#  The right subtree of a node contains only nodes with keys greater than or 
# equal to the node's key. 
#  Both the left and right subtrees must also be binary search trees. 
#  
# 
#  
#  Example 1: 
#  
#  
# Input: root = [1,null,2,2]
# Output: [2]
#  
# 
#  Example 2: 
# 
#  
# Input: root = [0]
# Output: [0]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the tree is in the range [1, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  
# 
#  
# Follow up: Could you do that without using any extra space? (Assume that the 
# implicit stack space incurred due to recursion does not count).
# 
#  Related Topics Tree Depth-First Search Binary Search Tree Binary Tree 👍 2762
#  👎 635


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.pre = None
        self.count = 0
        self.result = []
        self.maxCount = 0

    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        self.searchBST(root)
        return self.result

    def searchBST(self, root):
        if not root:
            return
        self.searchBST(root.left)
        if not self.pre:
            self.count = 1
        elif self.pre.val == root.val:
            self.count += 1
        else:
            self.count = 1
        if self.count == self.maxCount:
            self.result.append(root.val)
        if self.count > self.maxCount:
            self.result.clear()
            self.result.append(root.val)
            self.maxCount = self.count
        self.pre = root
        self.searchBST(root.right)

# leetcode submit region end(Prohibit modification and deletion)
