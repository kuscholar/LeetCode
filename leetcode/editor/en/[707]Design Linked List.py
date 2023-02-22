# Design your implementation of the linked list. You can choose to use a singly 
# or doubly linked list. A node in a singly linked list should have two 
# attributes: val and next. val is the value of the current node, and next is a pointer/
# reference to the next node. If you want to use the doubly linked list, you will 
# need one more attribute prev to indicate the previous node in the linked list. 
# Assume all nodes in the linked list are 0-indexed. 
# 
#  Implement the MyLinkedList class: 
# 
#  
#  MyLinkedList() Initializes the MyLinkedList object. 
#  int get(int index) Get the value of the indexᵗʰ node in the linked list. If 
# the index is invalid, return -1. 
#  void addAtHead(int val) Add a node of value val before the first element of 
# the linked list. After the insertion, the new node will be the first node of the 
# linked list. 
#  void addAtTail(int val) Append a node of value val as the last element of 
# the linked list. 
#  void addAtIndex(int index, int val) Add a node of value val before the indexᵗ
# ʰ node in the linked list. If index equals the length of the linked list, the 
# node will be appended to the end of the linked list. If index is greater than the 
# length, the node will not be inserted. 
#  void deleteAtIndex(int index) Delete the indexᵗʰ node in the linked list, if 
# the index is valid. 
#  
# 
#  
#  Example 1: 
# 
#  
# Input
# ["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", 
# "deleteAtIndex", "get"]
# [[], [1], [3], [1, 2], [1], [1], [1]]
# Output
# [null, null, null, null, 2, null, 3]
# 
# Explanation
# MyLinkedList myLinkedList = new MyLinkedList();
# myLinkedList.addAtHead(1);
# myLinkedList.addAtTail(3);
# myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
# myLinkedList.get(1);              // return 2
# myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
# myLinkedList.get(1);              // return 3
#  
# 
#  
#  Constraints: 
# 
#  
#  0 <= index, val <= 1000 
#  Please do not use the built-in LinkedList library. 
#  At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and 
# deleteAtIndex. 
#  
# 
#  Related Topics Linked List Design 👍 2020 👎 1379


# leetcode submit region begin(Prohibit modification and deletion)
class ListNode:
    def __init__(self, val=0, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class MyLinkedList:

    def __init__(self):
        self.dummyHead = ListNode()
        self.size = 0
        self.dummyTail = ListNode()
        self.dummyHead.next = self.dummyTail
        self.dummyTail.prev = self.dummyHead

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        current = self.dummyHead
        for _ in range(index):
            current = current.next
        return current.next.val

    def addAtHead(self, val: int) -> None:
        temp = self.dummyHead.next
        self.dummyHead.next = ListNode(val, temp, self.dummyHead)
        temp.prev = self.dummyHead.next
        self.size += 1
        print(self.size)

    def addAtTail(self, val: int) -> None:
        temp = self.dummyTail.prev
        self.dummyTail.prev = ListNode(val, self.dummyTail, temp)
        temp.next = self.dummyTail.prev
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0 or index > self.size:
            return
        current = self.dummyHead
        for _ in range(index):
            current = current.next
        temp = current.next
        current.next = ListNode(val, temp, current)
        temp.prev = current.next
        self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        current = self.dummyHead
        for _ in range(index):
            current = current.next
        current.next = current.next.next
        current.next.prev = current
        self.size -= 1

# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# leetcode submit region end(Prohibit modification and deletion)
