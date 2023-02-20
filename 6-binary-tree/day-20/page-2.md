# 700. Search in a Binary Search Tree

{% embed url="https://leetcode.com/problems/search-in-a-binary-search-tree/" %}

You are given the `root` of a binary search tree (BST) and an integer `val`.

Find the node in the BST that the node's value equals `val` and return the subtree rooted with that node. If such a node does not exist, return `null`.

**Example 1:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree1.jpg)

<pre><code><strong>Input: root = [4,2,7,1,3], val = 2
</strong><strong>Output: [2,1,3]
</strong></code></pre>

**Example 2:**

![](https://assets.leetcode.com/uploads/2021/01/12/tree2.jpg)

<pre><code><strong>Input: root = [4,2,7,1,3], val = 5
</strong><strong>Output: []
</strong></code></pre>

**Constraints:**

* The number of nodes in the tree is in the range `[1, 5000]`.
* `1 <= Node.val <= 107`
* `root` is a binary search tree.
* `1 <= val <= 107`

Related Topics

* Tree
* Binary Search Tree
* Binary Tree

\


* 👍 4599
* 👎 163



## Solution

```python
# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)
# leetcode submit region end(Prohibit modification and deletion)
```

