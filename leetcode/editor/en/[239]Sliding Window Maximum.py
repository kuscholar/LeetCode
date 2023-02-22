# You are given an array of integers nums, there is a sliding window of size k 
# which is moving from the very left of the array to the very right. You can only 
# see the k numbers in the window. Each time the sliding window moves right by one 
# position. 
# 
#  Return the max sliding window. 
# 
#  
#  Example 1: 
# 
#  
# Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
# Output: [3,3,5,5,6,7]
# Explanation: 
# Window position                Max
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  Example 2: 
# 
#  
# Input: nums = [1], k = 1
# Output: [1]
#  
# 
#  
#  Constraints: 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  1 <= k <= nums.length 
#  
# 
#  Related Topics Array Queue Sliding Window Heap (Priority Queue) Monotonic 
# Queue 👍 13618 👎 440


# leetcode submit region begin(Prohibit modification and deletion)
from collections import deque
class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        # only popleft if the leftmost value in the window is the front of the current MyQueue,
        # otherwise it means the value to be popped is not the largest, the current front is within the window
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if not nums or not k:
            return []
        result = []
        queue = MyQueue()
        for i in range(k):
            queue.push(nums[i])
        result.append(queue.front())
        for i in range(k, len(nums)):
            queue.pop(nums[i-k])
            queue.push(nums[i])
            result.append(queue.front())
        return result

# leetcode submit region end(Prohibit modification and deletion)
