# Given the head of a linked list, remove the nᵗʰ node from the end of the list 
# and return its head. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4,5], n = 2
# Output: [1,2,3,5]
#  
# 
#  Example 2: 
# 
#  
# Input: head = [1], n = 1
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1,2], n = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is sz. 
#  1 <= sz <= 30 
#  0 <= Node.val <= 100 
#  1 <= n <= sz 
#  
# 
#  
#  Follow up: Could you do this in one pass? 
# 
#  Related Topics Linked List Two Pointers 👍 14629 👎 606


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not n or n < 0:
            return head
        dummy = ListNode(next=head)
        slow = fast = dummy
        for _ in range(n+1):
            if not fast:
                return head
            fast = fast.next
        while fast:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
