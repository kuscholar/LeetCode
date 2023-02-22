# Given a linked list, swap every two adjacent nodes and return its head. You 
# must solve the problem without modifying the values in the list's nodes (i.e., 
# only nodes themselves may be changed.) 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
#  
# 
#  Example 2: 
# 
#  
# Input: head = []
# Output: []
#  
# 
#  Example 3: 
# 
#  
# Input: head = [1]
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of nodes in the list is in the range [0, 100]. 
#  0 <= Node.val <= 100 
#  
# 
#  Related Topics Linked List Recursion 👍 9042 👎 352


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(next=head)
        prev = dummy
        while head and head.next:
            temp = head.next.next
            head.next.next = head
            prev.next = head.next
            head.next = temp
            prev = head
            head = head.next
        return dummy.next


# leetcode submit region end(Prohibit modification and deletion)
