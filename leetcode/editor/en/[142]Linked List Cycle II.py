# Given the head of a linked list, return the node where the cycle begins. If 
# there is no cycle, return null. 
# 
#  There is a cycle in a linked list if there is some node in the list that can 
# be reached again by continuously following the next pointer. Internally, pos is 
# used to denote the index of the node that tail's next pointer is connected to (0
# -indexed). It is -1 if there is no cycle. Note that pos is not passed as a 
# parameter. 
# 
#  Do not modify the linked list. 
# 
#  
#  Example 1: 
#  
#  
# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the 
# second node.
#  
# 
#  Example 2: 
#  
#  
# Input: head = [1,2], pos = 0
# Output: tail connects to node index 0
# Explanation: There is a cycle in the linked list, where tail connects to the 
# first node.
#  
# 
#  Example 3: 
#  
#  
# Input: head = [1], pos = -1
# Output: no cycle
# Explanation: There is no cycle in the linked list.
#  
# 
#  
#  Constraints: 
# 
#  
#  The number of the nodes in the list is in the range [0, 10⁴]. 
#  -10⁵ <= Node.val <= 10⁵ 
#  pos is -1 or a valid index in the linked-list. 
#  
# 
#  
#  Follow up: Can you solve it using O(1) (i.e. constant) memory? 
# 
#  Related Topics Hash Table Linked List Two Pointers 👍 10116 👎 737


"""
every step slow goes, fast goes two
length(fast) = 2*length(slow)
length(fast) = x + y + n*(y + z)
length(slow) = x + y
x + y + n*(y + z) = 2 *(x + y)
assume n = 1,
x = z, which means if now slow stays where it is, and fast moves back to the start,
and they move the same step each time, they will meet again at the entrance of the cycle

那么 n如果大于1是什么情况呢，就是fast指针在环形转n圈之后才遇到 slow指针。

其实这种情况和n为1的时候 效果是一样的，一样可以通过这个方法找到 环形的入口节点，只不过，index1
指针在环里 多转了(n-1)圈，然后再遇到index2，相遇点依然是环形的入口节点。
"""

# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        dummy = ListNode(next=head)
        slow = fast = dummy
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            # NOTE: must check this after the first move, otherwise will break cuz they were dummy
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        fast = dummy
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow

# leetcode submit region end(Prohibit modification and deletion)
